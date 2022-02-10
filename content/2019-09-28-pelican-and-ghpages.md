---
title: Pelican and GitHub Pages 
author: Laura Santamaria
category: meta-stuff
slug: pelican-and-ghpages
date: 28 September 2019
tags: blog, meta, pelican, github
status: published
---

I thought I'd throw together a quick post on using Pelican with GitHub Pages and GitHub Actions.

I decided to use a Python-based static-site generator instead of Jekyll because (a) I love Python and (2) Ruby and I aren't always on the best of terms. In addition, I wanted a system that I could really dig into and throw plugins together whenever I wanted. In another job, I managed a custom Jekyll system with plugins and hooks that I built myself, but I know doing that sort of thing in Ruby would take me a lot longer than just knocking it together in Python. Perhaps in the future I'll build the site with a different system depending on how complex it gets, but a simple static-site generator really has a lot of appeal for something this simple. I chose Pelican mainly because I wanted to figure out how it worked; nothing Earth-shattering there.

The biggest challenge I had was automating publication of the site to GitHub Pages. I wanted to be able to write a post on my phone on a plane and be able to publish that post from my phone without the ability to build the site locally. I certainly could have done that with a more traditional content management system (CMS) like Ghost or (*shudder*) Wordpress. However, there was an appealing challenge in making it work, and I admit to jumping at the chance to try GitHub Actions. So I started getting the site in order locally, and then I joined the beta for Actions to get started.

First, I needed to trigger a build when a push goes the right branch. I decided to have a different host branch for the source code of the site since user pages on GitHub require publishing from master in a specially named repo. So my workflow had to trigger from a different branch:

```yaml
on:
  push:
    branches:
      - source
```

I decided on an Ubuntu image to build on as I run Ubuntu at home, and therefore the build should be fairly close to my local builder. Everything from here on are job steps.

Next, I had to check out that specific branch. I borrowed an Action to make that happen:

```yaml
    - uses: actions/checkout@v1
```

Then, the workflow needed to set up the overall environment:

```yaml
    - name: Set up Python 3.7
      uses: actions/setup-python@v1
      with:
        python-version: 3.7
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
```

Next, a make command! The Makefile ensures that I don't have to remember all of my options I run, and that means a more consistent build when I *do* run it on my local system.

```yaml
    - name: Build the prod site
      run: |
        make publish
```

This next bit is really, really important for publishing to GitHub Pages, and it's a bit silly of a step, really. You need to stop Jekyll from trying to parse your new raw HTML files and failing. The way to do that on GitHub Pages is an empty file named `.nojekyll`. So, a quick touch command to the designated output directory for the publish build before moving it to the master branch, and we're ready for publication:

```yaml
    - name: Add nojekyll
      run: |
        touch ./output/.nojekyll
```

Finally, deployment time! We just need to send the raw HTML from the output directory to the master branch. However, I had to find a good Action to do it because I have a custom domain. All of the other Actions I tried actually broke my custom domain, so this one actually adds the custom domain designation every time. The creator (see the `uses` value) made some clear docs around the Action, too, which makes me very happy.

```yaml
    - name: Deploy to GitHub Pages
      uses: JamesIves/github-pages-deploy-action@master
      if: success()
      env:
        ACCESS_TOKEN: ${{ secrets.GH_PAT }}
        BASE_BRANCH: source # The branch the action should deploy from.
        BRANCH: master # The branch the action should deploy to.
        CNAME: nimbinatus.com
        FOLDER: output # The folder the action should deploy.
```

So there you have it. I just push changes like this post to my source branch, and GitHub Actions publishes the whole thing for me. And all on the back of Python, which makes me happy.

Check out the full workflow in [my repo](https://github.com/nimbinatus/nimbinatus.github.io/blob/source/.github/workflows/pelican.yml). Questions? Feel free to reach out to me on [Twitter](https://twitter.com/nimbinatus).