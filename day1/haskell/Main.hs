module Main where

main :: IO ()
main = do
  inputs <- lines <$> readFile "../input.txt"
  let out = map read inputs :: [Int]
  let res = head [a*b | a <- out, b <- out, a + b == 2020]
  print res

