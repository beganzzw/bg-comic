"""Build a portable, image-first comic preview with the Python standard library."""
import argparse
import html
from pathlib import Path
import shutil
import zipfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--title', required=True)
    parser.add_argument('--images', nargs='+', required=True)
    parser.add_argument('--output-dir', required=True)
    args = parser.parse_args()
    sources = [Path(p).resolve() for p in args.images]
    for source in sources:
        if not source.is_file():
            parser.error('Image does not exist: ' + str(source))
    out = Path(args.output_dir).resolve()
    out.mkdir(parents=True, exist_ok=True)
    targets = [out / ('%02d%s' % (i, p.suffix.lower())) for i, p in enumerate(sources, 1)]
    page = out / 'index.html'
    archive = out / 'comic-package.zip'
    if any(p.exists() for p in targets + [page, archive]):
        parser.error('Output already exists; choose a new output directory to preserve previous versions.')
    for source, target in zip(sources, targets):
        shutil.copy2(source, target)
    title = html.escape(args.title)
    figures = '\n'.join('<img src="%s" alt="漫画第%d页">' % (p.name, i) for i, p in enumerate(targets, 1))
    page.write_text('''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>''' + title + '''</title>
<style>body{margin:0;background:#faf7ef;color:#222;font-family:system-ui,"Microsoft YaHei",sans-serif}main{max-width:760px;margin:auto;padding:28px 16px 48px}h1{font-size:28px;line-height:1.5;margin:0 0 24px}img{display:block;width:100%;height:auto;margin:0 0 20px}</style>
</head><body><main><h1>''' + title + '</h1>\n' + figures + '</main></body></html>', encoding='utf-8')
    with zipfile.ZipFile(archive, 'w', zipfile.ZIP_DEFLATED) as z:
        for p in [page] + targets:
            z.write(p, p.name)
    print(str(page))
    print(str(archive))


if __name__ == '__main__':
    main()
