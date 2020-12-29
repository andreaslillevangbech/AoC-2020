solve :: [Int] -> Int
solve (n:ns) | elem (2020 - n) ns = n * (2020-n)
             | otherwise          = solve ns
solve _ = error " Not Found "

solve2 :: [Int] -> Int
solve2 ns = head [a*b*c | a <- ns, b <- ns, c <- ns, a+b+c==2020]

main :: IO ()
main = print =<< solve2 . map read . lines <$> readFile "input"
