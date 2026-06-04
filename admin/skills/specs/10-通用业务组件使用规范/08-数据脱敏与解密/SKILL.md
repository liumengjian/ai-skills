---
name: jjb-desensitization
description: 数据脱敏与解密查看规范。适用场景：展示加密的敏感数据（姓名、手机号、身份证号、图片等），并提供点击解密查看明文的能力。不限于表格，表单、详情页等场景均可使用。
---

# 通用业务组件使用规范

## 数据脱敏与解密

脱敏数据在后端以密文存储，前端拿到的数据包含脱敏后的展示文本和加密串。对于有解密权限的数据，用户可**点击解密查看明文**。

### 数据格式

后端返回的脱敏数据为对象结构，各场景统一使用此格式：

| 字段 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `flag` | `'TRUE'` \| `'FALSE'` | ✅ | 是否为加密数据。`'TRUE'` 时可解密查看，`'FALSE'` 时仅展示脱敏文本 |
| `label` | `string` | ✅ | 脱敏后的展示文本（如 `张**`、`138****1234`） |
| `value` | `string` | ✅ | 加密串，用于调用解密接口 |
| `type` | `string` | ✅ | 数据类型枚举：`CHINESE_NAME` / `MOBILE_PHONE` / `ID_CARD` / `PICTURE` 等 |

```json
{
  "flag": "TRUE",
  "label": "张**",
  "value": "encrypted_string_here...",
  "type": "CHINESE_NAME"
}
```

> 若 `content` 为普通字符串（非对象），说明数据未脱敏，直接展示即可。

### 解密接口

#### 请求方式

```javascript
import { http } from '@cqsjjb/jjb-common-lib';

const res = await http.Post('@/user/desensitizations/client/decrypt/one', {
  maskDTO: content,     // 脱敏数据对象 { flag, label, value, type }
  fieldKey: fieldKey    // 字段标识，一般传表单字段名（如表单场景下的 name 属性值）
});
```

#### 参数说明

| 参数 | 类型 | 必填 | 说明 |
|------|------|------|------|
| `maskDTO` | `Object` | ✅ | 完整的脱敏数据对象，即接口返回的原始 content |
| `fieldKey` | `string` | ✅ | 字段标识，一般对应表单字段名。如表单字段 `name="userName"`，则传 `"userName"` |

#### 响应处理

```javascript
import { tools } from '@cqsjjb/jjb-common-lib';

if (res.success) {
  const decodedData = tools.toObject(tools.toObject(res.data).maskDTO);
  const plainText = decodedData?.label || null;   // 解密后的明文
}
```

### 交互模式

适用于**任意场景**（表格、表单、详情页等），核心交互一致：

#### 脱敏态（默认）

- 展示 `label`（脱敏文本）
- `*` 号超过 5 个时折叠为 5 个（`*****`），避免展示过长
- 若 `flag === 'TRUE'`，展示眼睛图标 `<EyeOutlined />`，提示可解密查看
- 若 `flag === 'FALSE'`，不展示图标，仅展示脱敏文本

#### 解密态（点击后）

- 发起解密接口请求，期间 `<Spin>` 展示加载状态
- 解密成功后切换展示明文，图标变为 `<EyeInvisibleOutlined />`
- 点击隐藏图标切回脱敏态，再次查看使用缓存，不重复请求接口

#### 图片脱敏

- 展示不可识别的占位缩略图
- 点击预览时自动触发解密，展示真实图片
- 关闭预览时清理解密数据

```jsx
// 文本脱敏 — 交互骨架
const [showDecode, setShowDecode] = useState(false);
const [decodeData, setDecodeData] = useState(null);
const [loading, setLoading] = useState(false);

const decrypt = async () => {
  if (decodeData) {
    setShowDecode(true);          // 已有缓存，直接展示
    return;
  }
  setLoading(true);
  const res = await http.Post('@/user/desensitizations/client/decrypt/one', {
    maskDTO: content,
    fieldKey: fieldKey,
  });
  setLoading(false);
  if (res.success) {
    const decoded = tools.toObject(tools.toObject(res.data).maskDTO);
    setDecodeData(decoded?.label || null);
    setShowDecode(true);
  }
};

// 脱敏态
<Space>
  <span>{maskedLabel}</span>
  <Spin spinning={loading}>
    {content.flag === 'TRUE' && <EyeOutlined onClick={decrypt} />}
  </Spin>
</Space>

// 解密态
<Space>
  <span>{decodeData}</span>
  <EyeInvisibleOutlined onClick={() => setShowDecode(false)} />
</Space>
```

### 注意事项

- 解密接口调用可能较慢，**必须**有 Loading 状态反馈
- 解密成功后缓存结果，避免重复请求
- 解密失败时静默处理，不切换展示状态
- 该模式不仅限于表格列，表单回填、详情展示等场景均可复用
