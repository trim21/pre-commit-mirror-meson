meson mirror
===================

Mirror of `meson` package for pre-commit.

For pre-commit: see https://github.com/pre-commit/pre-commit

For meson: see https://github.com/mesonbuild/meson

### Using meson with pre-commit

Add this to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/trim21/pre-commit-mirror-meson
  rev: ''  # Use the sha / tag you want to point at
  hooks:
    - id: meson-fmt
      args: ['--inplace'] # format file in place
    - id: meson-fmt
      args: ['--check-only'] # do check only
```
