main :: IO ()
main = do
  inputs <- lines <$> readFile "../input"
  print $ length . filter (=='#') . zipWith (flip (!!)) [0,3..] . map cycle inputs
