# 🎮 水果消消乐 PK 版 - 微信小游戏

> 网红萌宠 + 双人 PK + 炫酷特效 🦦🐧🎯

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![WeChat](https://img.shields.io/badge/Platform-WeChat-green.svg)](https://developers.weixin.qq.com/miniprogram/dev/framework/)

## ✨ 全新特性

### 🎨 1. 优化界面设计
- 渐变色彩 + 圆角卡片
- 流畅动画效果
- 响应式布局

### ⚔️ 2. 双人 PK 模式
- 微信好友联机对战
- 实时分数比拼
- PK 排行榜

### 🐾 3. 网红萌宠主题
| 主题 | 角色 | 说明 |
|------|------|------|
| 🦦 | 哈吉米 | 网红水豚 |
| 🐧 | 企鹅 | 呆萌企鹅 |
| 🐰 | Doro | 热门兔兔 |
| 🐱 | 猫猫 | 经典猫咪 |
| 🐶 | 狗狗 | 可爱小狗 |
| 💣 | 炸弹 | 特殊道具 |

### 💣 4. 炸弹道具
- 点击消除周围 3x3 区域
- 误点炸弹直接失败
- 紧张刺激！

### 🎯 5. 特殊效果
- **范围炮** - 消除周围 8 格
- **语音嘲讽** - 经典网络用语
- **表情包** - 搞笑表情动画

### 📊 6. 排行榜
- 好友排行
- 历史最高分
- PK 战绩

## 🚀 快速开始

### 方式 1: 微信开发者工具
```
1. 下载 https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html
2. 导入 game-miniprogram 目录
3. 填入 AppID
4. 编译运行
```

### 方式 2: 真机预览
```
1. 开发者工具 → 预览
2. 扫码在手机上运行
```

## 📁 项目结构

```
fruit-elimination-game/
├── game-miniprogram/       # 小程序主目录
│   ├── app.js              # 入口文件
│   ├── app.json            # 配置文件
│   ├── app.wxss            # 全局样式
│   ├── pages/
│   │   ├── index/          # 首页
│   │   ├── game/           # 游戏页
│   │   ├── result/         # 结果页
│   │   ├── pk/             # PK 对战
│   │   └── rank/           # 排行榜
│   ├── utils/              # 工具函数
│   ├── images/             # 图片资源
│   └── components/         # 组件
├── README.md
└── LICENSE
```

## 🎮 游戏规则

### 经典模式
1. 点击相邻相同角色进行消除
2. 每次消除获得分数
3. 达到目标分数通关
4. 避免点到炸弹！

### PK 模式
1. 邀请微信好友对战
2. 双方同时游戏
3. 先达到目标分数者胜
4. 失败者接受表情包嘲讽

## 🎯 特殊道具

| 道具 | 效果 | 获取方式 |
|------|------|----------|
| 💣 炸弹 | 消除 3x3 | 随机出现 |
| 🎯 范围炮 | 消除周围 8 格 | 连续消除 |
| 📢 嘲讽 | 干扰对手 | PK 模式 |
| ⏰ 加时 | +10 秒 | 特殊成就 |

## 🛠️ 技术栈

- 微信小程序原生开发
- Canvas 动画渲染
- WebSocket 实时通信
- 云开发数据库

## 📄 License

MIT License

## 👤 作者

养虾哥 🦐

---

Made with ❤️ for 消除游戏爱好者
