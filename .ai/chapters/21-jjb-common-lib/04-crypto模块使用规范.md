# 二十五、crypto 模块使用规范

## 1. 概述

`crypto` 模块是 `@cqsjjb/jjb-common-lib` 通用工具库中的加解密模块，基于 cryptojs 实现，提供 AES-128 加解密和 MD5 哈希功能。

### 1.1 导入方式

```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';
```

## 2. 内置方法详解

### 2.1 AES_128_Encrypt(content)

AES-128 位加密。

**参数：**
- `content` (string): 待加密内容

**返回值：**
- `string`: 加密后的字符串

**示例：**
```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';

// 加密字符串
const encrypted = crypto.AES_128_Encrypt('123');
console.log(encrypted); // 输出加密后的字符串

// 加密敏感信息
const password = crypto.AES_128_Encrypt('myPassword123');
```

**使用场景：**
- 加密敏感数据（如密码、身份证号等）
- 加密需要传输的敏感信息
- 数据存储前的加密处理

**注意事项：**
- 加密后的字符串长度会比原字符串长
- 相同的输入每次加密结果可能不同（如果使用了随机 IV）
- 加密后的数据需要使用对应的解密方法才能还原

### 2.2 AES_128_Decrypt(content)

AES-128 位解密。

**参数：**
- `content` (string): 已加密内容

**返回值：**
- `string`: 解密后的字符串

**示例：**
```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';

// 解密字符串
const encrypted = 'xxxxxx'; // 加密后的字符串
const decrypted = crypto.AES_128_Decrypt(encrypted);
console.log(decrypted); // 输出解密后的原始内容

// 解密密码
const encryptedPassword = '...'; // 从服务器获取的加密密码
const password = crypto.AES_128_Decrypt(encryptedPassword);
```

**使用场景：**
- 解密从服务器获取的加密数据
- 解密本地存储的加密信息
- 解密传输过程中加密的数据

**注意事项：**
- 只能解密使用 `AES_128_Encrypt` 加密的数据
- 如果加密内容格式不正确，解密可能失败
- 确保加密和解密使用相同的密钥和算法配置

### 2.3 MD5(content)

MD5 哈希加密。

**参数：**
- `content` (string): 待加密内容

**返回值：**
- `string`: MD5 字符串（32 位十六进制字符串）

**示例：**
```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';

// MD5 加密
const hash = crypto.MD5('123');
console.log(hash); // => "202cb962ac59075b964b07152d234b70"

// 加密密码（用于密码校验）
const password = 'userPassword';
const passwordHash = crypto.MD5(password);
console.log(passwordHash);

// 生成文件哈希
const fileContent = 'file content here';
const fileHash = crypto.MD5(fileContent);
```

**使用场景：**
- 密码哈希存储（单向加密，不可逆）
- 数据完整性校验
- 生成唯一标识符
- 文件内容校验

**注意事项：**
- MD5 是单向哈希函数，无法解密还原原始内容
- 相同的输入总是产生相同的输出
- MD5 已不推荐用于密码存储（建议使用更安全的算法如 bcrypt），但仍可用于数据校验

## 3. 使用示例

### 3.1 密码加密存储

```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';

// 用户注册时加密密码
function registerUser(username, password) {
  // 使用 MD5 加密密码（注意：实际项目中应使用更安全的算法）
  const passwordHash = crypto.MD5(password);
  
  // 发送到服务器
  return http.Post('/api/register', {
    username,
    password: passwordHash
  });
}
```

### 3.2 敏感数据加密传输

```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';

// 加密敏感信息后传输
function submitSensitiveData(data) {
  const encryptedData = crypto.AES_128_Encrypt(JSON.stringify(data));
  
  return http.Post('/api/submit', {
    encryptedData
  });
}
```

### 3.3 数据解密处理

```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';

// 从服务器获取加密数据并解密
function getDecryptedData() {
  return http.Get('/api/data')
    .then(res => {
      if (res.success) {
        // 解密数据
        const decrypted = crypto.AES_128_Decrypt(res.data.encryptedContent);
        return JSON.parse(decrypted);
      }
    });
}
```

### 3.4 数据完整性校验

```javascript
import { crypto } from '@cqsjjb/jjb-common-lib';

// 校验数据是否被篡改
function verifyData(data, expectedHash) {
  const dataHash = crypto.MD5(JSON.stringify(data));
  return dataHash === expectedHash;
}

// 使用示例
const data = { id: 1, name: 'test' };
const hash = crypto.MD5(JSON.stringify(data));

// 传输后校验
const isValid = verifyData(data, hash);
console.log('数据完整性:', isValid);
```

## 4. 安全注意事项

### 4.1 AES 加密

- **密钥管理**：确保加密密钥的安全存储，不要硬编码在代码中
- **IV（初始化向量）**：如果使用随机 IV，需要将 IV 与密文一起存储
- **算法选择**：AES-128 适用于大多数场景，如需更高安全性可使用 AES-256

### 4.2 MD5 哈希

- **密码存储**：不推荐使用 MD5 存储密码，建议使用 bcrypt、argon2 等专门用于密码的哈希算法
- **碰撞风险**：MD5 存在碰撞风险，不适合用于安全关键场景
- **数据校验**：MD5 仍可用于数据完整性校验和生成唯一标识符

### 4.3 最佳实践

1. **敏感数据**：使用 AES 加密存储和传输敏感数据
2. **密码处理**：使用专门的密码哈希算法（如 bcrypt），而不是 MD5
3. **密钥管理**：密钥应存储在安全的地方，不要暴露在前端代码中
4. **错误处理**：加密/解密失败时应妥善处理错误，不要暴露敏感信息

## 5. 相关模块

- **详细文档**：参考 `reference/crypto.d.ts` 查看完整的类型定义和 API 文档
- **底层实现**：基于 cryptojs 库实现

## 6. 常见问题

### 6.1 加密后数据长度变化

AES 加密后的数据长度会变化，通常比原数据长。这是因为：
- 加密算法会对数据进行填充
- 可能包含 IV（初始化向量）
- Base64 编码会增加长度

### 6.2 加密结果不一致

如果相同的输入产生不同的加密结果，这是正常的，因为：
- 使用了随机 IV（初始化向量）
- 这是加密算法的安全特性

### 6.3 MD5 不可逆

MD5 是单向哈希函数，无法从哈希值还原原始内容。如果需要可逆加密，应使用 AES 加密。

## 7. 注意事项

1. **安全性**：前端加密不能完全保证数据安全，敏感操作应在后端进行

2. **性能**：加密/解密操作有一定性能开销，避免在高频操作中使用

3. **兼容性**：确保在支持的浏览器环境中使用，现代浏览器都支持

4. **错误处理**：加密/解密可能失败，应添加适当的错误处理

5. **密钥管理**：不要在前端代码中硬编码密钥，密钥应由后端管理或通过安全方式传递
