# lookatme.contrib.notes

Simplistic speaker notes

## Installation

If this project has been pushed up to pypi:

```bash
pip install lookatme.contrib.notes
```

otherwise:

```bash
pip install ./path/to/lookatme.contrib.notes
```

## Usage

Add the notes into the extensions array in the
slide YAML header:

```markdown
---
title: A title
author: Me
date: 2019-12-04
extensions:
  - notes
---
```

With the extension installed and declared in the YAML header, use it in your
markdown like so:

~~~markdown
```notes

```
~~~
