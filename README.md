# Build-Build-Revolution (BBR)
Learning a new build order in Starcraft 2 can be tricky, so I made this
tool to make it a little easier. Just load up a replay file where the
first human player is playing a build-order you want to practice. Once
the build is loaded, you'll see a visual timeline of all of the unit,
structure, and upgrade timings. Just hit play and run it on your second
monitor while you practice against the AI!
## installation
BBR is written as a Python 3.x [FastAPI](https://fastapi.tiangolo.com/)
application. I host it with [uvicorn](https://www.uvicorn.org/), and
have successfully hosted it on both Windows and Linux.

1) Install uvicorn using your preferred mode (pure Python or Cython-based,
see the uvicorn documentation).
2) Install python dependencies with:
```
python -m pip install -r requirements.txt
```
## running
You should be able to run the server from the command line:
```
uvicorn server:app
```
If you are doing development, consider adding the `--reload` option
which will cause uvicorn to auto-reload if you make any source changes:
```
uvicorn server:app --reload
```

## license
MIT License

Copyright (c) 2022 Scott Means

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
