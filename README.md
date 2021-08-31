# aws-firehose-to-flat-json

[![CI](https://github.com/worldpwn/aws-firehose-to-flat-json/actions/workflows/ci.yml/badge.svg)](https://github.com/worldpwn/aws-firehose-to-flat-json/actions/workflows/ci.yml)

It will convert an array of objects into flatten data. 
Use stringifyLevel to set the level at which the rest of the data will be JSON stringify.

## Example with stringifyLevel 2

It will convert json like this:

<img width="311" alt="Screenshot 2021-07-14 at 09 42 13" src="https://user-images.githubusercontent.com/6351780/131465627-31672ccc-7921-4c92-b1f0-1967ba843fef.png">

to this:

<img width="385" alt="Screenshot 2021-07-14 at 09 44 14" src="https://user-images.githubusercontent.com/6351780/131465658-86ff64cb-d117-4564-9930-91c964320f2f.png">
