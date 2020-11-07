# Magic Strings

Der Text besteht nur aus Zahlen, klein und Großbuchstaben. Am Ende ist ein `=`, was auf [BASE64](https://de.wikipedia.org/wiki/Base64) zuschließen lässt (`=` am Ende ist ein typisches Füllzeichen dafür).
Mittlerweile wird die Mathematik zu aufwändig, das ganze im Kopf zu machen, ich rate dringend zu einem Decoder. Unter Linux im Terminal folgendes: `echo "BASE64String" | base64 -d`. Alternativ kann man auch einen online Decoder verwenden.

Das Flag ist `JHHDCTF{base64_is_very_cool}`
