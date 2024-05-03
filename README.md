Pinyin to X-SAMPA
=================

This program converts Pinyin (Mandarin Chinese) to X-SAMPA phonetic symbols.


The output X-SAMPA standard is fully compatible with **Synthesizer V Studio Phoneme Reference (1.11.0 update)**, which can be found at https://www.dreamtonics.com.cn/svstudio-resources/. A json file is included in the repository as a reference lookup table for common Pinyin to X-SAMPA phonetic symbols, but it is not used directly in the project's code.


Released under LGPL 3.0 and above version.


Usage
-----

The C++ version was still under development. The Python version is available.


For the Python version, use a Python 3 or newer interpreter to run it.


Input with Pinyin separated with a space between each word, and the output will be X-SAMPA phonetic symbols.


Development Plan
-----

- [x] This project aims to change the X-SAMPA standard to the one used by Synthesizer V.
- [ ] Add support for file input and output.
- [ ] Add support for Chinese characters input.


ACKNOWLEDGEMENTS
-----

This project is a fork of [pinyin2xsampa](https://github.com/m13253/pinyin2xsampa), originally developed by [Star Brilliant](https://github.com/m13253). Thanks to Brilliant for the original work and for sharing the code, which has been an essential starting point for this extended project.