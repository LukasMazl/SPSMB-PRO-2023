# 3. Hodina

- Napište program, který bude mít dvě funkce. Funkci encode a decode. Funkce encode ma na vstupu 2 parametry. Klíč, pomocí kterého je zpráva zašifrována a původní text. Funkce by měla zašifrovat text pomocí Caesarovi šifry. Tj. pokud mám klíč 1 a zprávu "AZB", výsledkem bude "BAC". Je potřeba v tomto případě řešit posun. Také je nutné říci, že tato metoda platí pouze pro znaky. Pokud je znakem zavináč, mezera, nový řádek, čárka či tečka, tak jsou znaky ,,pouze opsány" na výstup.

- Napište program, který bude mít dvě funkce. Funkci encode a decode. Funkce encode ma na vstupu 2 parametry. Klíč, pomocí kterého je zpráva zašifrována a původní text. Implementuje Vernamovu šifru.

## Domácí úkol

Implementace RLE algoritmu. Tento algoritmus je kompresní a umožnuje zmenši objem dat např. u obázku.

Pokud mám tento řetezec "AAABBBCCCCCCD", tak výsledek po aplikování RLE je "3A3B6C1D". Stejně tak je nutné napsat funkci pro dekompresi.
