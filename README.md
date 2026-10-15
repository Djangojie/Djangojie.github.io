# Djangojie 的博客

这是 [Djangojie.github.io](https://Djangojie.github.io) 的 Jekyll 源码，使用 [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) 主题，由 GitHub Pages 构建和发布。

## 写文章

在 `_posts/` 新建 `YYYY-MM-DD-slug.md`，加入标题、北京时间和分类等 front matter，再写正文。文章中的项目状态应与对应仓库的 README、测试记录保持一致；演示原型、待实现功能和未验证结论要分别标明。

## 本地预览

需要 Ruby、Bundler 和 Jekyll 依赖：

```sh
bundle install
bundle exec jekyll serve
```

打开 `http://127.0.0.1:4000`。推送到 `main` 后，`.github/workflows/pages-deploy.yml` 会构建并部署站点。以 GitHub Actions 的运行结果和实际页面为发布验证依据。

## 仓库结构

- `_posts/`：文章。
- `_tabs/`：站点页面。
- `_config.yml`：站点信息与主题配置。
- `.github/workflows/`：Pages 构建流程。

主题由 [Chirpy Starter](https://github.com/cotes2020/chirpy-starter) 提供；仓库许可证见 [LICENSE](LICENSE)。
