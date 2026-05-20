# Usage Tutorial

## What this skill does

This skill helps generate Chinese HTML course pages in a consistent white, soft, minimal tech style.

It is especially useful when you want to paste HTML into a text file and open it in a browser as a presentation page.

## Recommended workflow

### Step 1: Give your idea or outline

Example prompt:

> 我想做一套给普通办公岗位看的 AI 课件，主题是“AI 不只是聊天，而是执行助理”。请先帮我规划大纲和每页内容，不要急着写 HTML。

The skill should first output:

- course positioning
- audience
- PART structure
- page-by-page plan
- visual suggestions

### Step 2: Confirm the plan

Reply:

> 同意，按这个规划开始生成 HTML。

Or provide changes:

> 第 3 部分太技术了，改得更适合非技术人员。

### Step 3: Generate pages

Example prompt:

> 请先生成第 1 页封面 HTML。

or

> 请生成 PART 1 的 5 个页面，每页单独输出完整 HTML。

### Step 4: Integrate pages into one scrolling HTML

After all pages are ready, ask:

> 请把第 1 页到第 27 页整合成一个滚动版 HTML，保留锚点导航、当前页高亮、滚动进度、键盘翻页、内容点击放大动效。

## Common prompt templates

### Generate one page

> 根据下面内容生成一页 16:9 HTML 课件页，保持白底、柔和、简约科技风。内容是：...

### Generate chapter page

> 生成一个章节页：PART 2 思维转变：从问问题，升级到交付任务。只展示章节信息，不要拓展多余内容。

### Generate ending page

> 生成一个结尾页，只需要一句话：从这一页开始，让 AI 为你干活，期待看到你的 AI 成果！

### Create integrated scrolling page

> 我上传了 27 个 HTML 页面，请按文件名顺序整合成一个 HTML。每页保持 16:9，增加顶部锚点导航、当前页高亮、滚动进度、键盘翻页和内容点击放大动效。
