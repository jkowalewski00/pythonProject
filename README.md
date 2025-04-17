
# Środowisko do badań jakościowych skuteczności algorytmów sztucznej inteligencji w rozpoznawaniu sposobów szyfrowania plików

Co zawierają poszczególne katalogi i pliki?

1. 1800_files - pliki w formatach *.txt, *.csv, *.py, *.html, *.bmp, *.wav, po 1800 na format.
2. 3000_files - pliki w formatach *.txt, *.csv, *.py, *.html, *.bmp, *.wav, po 3000 na format.
3. encrypted_ecb_1800 - pliki zaszyfrowane algorytmami AES, DES, 3DES i RC4 przy użyciu 1 klucza na algorytm i niezaszyfrowane, po 1800 na format, każdy format zaszyfrowany (i niezaszyfrowany) algorytmami proporcjonalnie.
4. encrypted_ecb_1800_3keys - pliki zaszyfrowane algorytmami AES, DES, 3DES i RC4 przy użyciu 3 kluczy na algorytm i niezaszyfrowane, po 1800 na format, każdy format zaszyfrowany (i niezaszyfrowany) algorytmami proporcjonalnie.
5. encrypted_ecb_1800_6keys - pliki zaszyfrowane algorytmami AES, DES, 3DES i RC4 przy użyciu 6 kluczy na algorytm i niezaszyfrowane, po 1800 na format, każdy format zaszyfrowany (i niezaszyfrowany) algorytmami proporcjonalnie.
6. encrypted_ecb_3000... - analogicznie jak wyżej, ale 3000 plików na format
7. encrypted_txts_1000_ecb - 1000 plików *.txt zaszyfrowanych algorytmami wg proporcji (projekt zespołowo-badawczy)
8. features_... - obliczone cechy zaszyfrowane plików zgodnie z powyższą konwencją
9. generated_txts_1000 - 1000 plików *txt wygenerowanych do projektu zespołowo-badawczego
10. ecb.ipynb - szyfrowanie plików w trubie ECB
11. experiment.ipynb - cały eksperyment przeprowadzony na 1000 plików *.txt
12. feature_extraction.ipynb - ekstrakcja cech zaszyfrowanych plików
13. files_generator.ipynb - generator plików
14. tests_ecb.ipynb - eksperyment w ramach pracy magisterskiej


## Authors

- [jkowalewski00](https://github.com/jkowalewski00)

