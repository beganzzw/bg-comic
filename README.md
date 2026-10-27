# Personal IP Comic

把真实经历、文章或选题逐步改编成有个人角色、有幽默对白的漫画图文。适用于支持 SKILL.md 的 Agent 环境。

## 一句话安装（推荐）

把下面这句话复制给你的 Agent：

> 请从 https://github.com/beganzzw/personal-ip-comic 安装 personal-ip-comic 技能到当前工具的用户级技能目录。先读取仓库说明，按当前环境适配安装路径，保留已有技能；安装后检查是否能识别，并告诉我如何调用。

Agent 需要具备网络访问和文件写入能力，并且宿主支持技能加载。不必手动下载 ZIP 或寻找目录。是否即时生效取决于宿主；如果需要刷新或重启会话，由 Agent 明确说明，不将文件复制成功当成已经加载。

## 工作流程

理解内容 → 确定大纲 → 选择风格与角色 → 分镜对白 → 样图 → 整套交付。

只读取当前阶段需要的说明。缺少角色图不会阻止讨论大纲；到视觉阶段才请用户上传或引用角色素材。已确认的选择不重复询问，明确要求一次完成时可合并阶段。

## 能力

- 支持黑白手稿、Scribble、治愈手绘、极简图解、活力手绘和白板风六种预设，也接受自定义风格。
- 未指定画风时先推荐并等待选择，不绑定默认个人IP。
- 适配当前 Agent 提供的生图能力及默认模型，无固定供应商、模型ID或本地服务依赖。
- 环境不能生图时直接交付逐页完整提示词，供用户复制到其他图片工具。
- 支持封面、气泡和文字验收、连续阅读HTML及ZIP素材包。
- 不自动发布到外部平台。

## 手动安装（备选）

将仓库作为一个完整的 `personal-ip-comic` 技能目录放入宿主的用户级 skills 目录。具体加载方式依宿主而定。

WorkBuddy 用户可将仓库复制到 `~/.workbuddy-ai/skills/personal-ip-comic/`。其他 Agent 请使用其文档规定的技能路径；本项目没有对所有宿主做端到端验证。

## 使用示例

> 使用 personal-ip-comic，把这段经历做成漫画。先给大纲，不生图。

> 大纲确认了，推荐一种适合轻松吐槽的画风。我会上传角色设定板。

> 按确认的对白先生成一张样图。环境不能生图就给我完整提示词。

## 文件结构

- `SKILL.md`：阶段路由与授权边界。
- `references/styles.md`：六种预设、自定义风格及覆盖规则。
- `references/playbook.md`：对白、提示词模板及检查说明。
- `references/image-capabilities.md`：宿主图片能力适配与无生图能力分支。
- `references/production.md`：样图、生成跟进、验收及交付。
- `scripts/build_preview.py`：仅用Python标准库构建可移动HTML与ZIP。

## 预览脚本

需要 Python 3.9 或更新版本，无第三方依赖。

```bash
python scripts/build_preview.py --title "我的漫画" --images /path/page1.png /path/page2.png --output-dir /path/new-output
```

输出目录应为空或全新；脚本拒绝覆盖同名成品。图片按顺序复制为01、02等文件名，输出 `index.html` 和 `comic-package.zip`。

## 素材与许可证

本仓库代码和技能文档采用 [MIT License](LICENSE)。不包含作者的个人IP图片、聊天截图、账号配置或凭证。使用者自行提供并确保有权使用角色与参考素材；MIT许可不授予链接指向的第三方素材、平台服务或模型的使用权。

风格分类灵感来源在 `references/styles.md` 列出，预设为独立整理，未打包或安装其链接中的第三方技能。
