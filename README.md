# Countdown
solving the challenge proposed in https://youtube.com/watch?v=X-7Wev90lw4&amp;feature=shares

# Sample output:
```
❯ python3 sol.py
smalls: [1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9, 10, 10]
total combinations: 15
(11, 36, 61, 86) with 0 large: 197557 out of 1306800 ( 15.1 % )
(11, 36, 61, 86) with 1 large: 473948 out of 2214000 ( 21.4 % )
(11, 36, 61, 86) with 2 large: 245653 out of 1134000 ( 21.7 % )
(11, 36, 61, 86) with 3 large: 33708 out of 198000 ( 17.0 % )
(11, 36, 61, 86) with 4 large: 956 out of 9000 ( 10.6 % )
(11, 36, 61, 86) in total: 951822 out of 4861800 ( 19.6 % )
(12, 37, 62, 87) with 0 large: 197557 out of 1306800 ( 15.1 % )
(12, 37, 62, 87) with 1 large: 472438 out of 2214000 ( 21.3 % )
(12, 37, 62, 87) with 2 large: 240421 out of 1134000 ( 21.2 % )
(12, 37, 62, 87) with 3 large: 32253 out of 198000 ( 16.3 % )
(12, 37, 62, 87) with 4 large: 887 out of 9000 ( 9.9 % )
(12, 37, 62, 87) in total: 943556 out of 4861800 ( 19.4 % )
(13, 38, 63, 88) with 0 large: 197557 out of 1306800 ( 15.1 % )
(13, 38, 63, 88) with 1 large: 478480 out of 2214000 ( 21.6 % )
(13, 38, 63, 88) with 2 large: 242020 out of 1134000 ( 21.3 % )
(13, 38, 63, 88) with 3 large: 32189 out of 198000 ( 16.3 % )
(13, 38, 63, 88) with 4 large: 895 out of 9000 ( 9.9 % )
(13, 38, 63, 88) in total: 951141 out of 4861800 ( 19.6 % )
(14, 39, 64, 89) with 0 large: 197557 out of 1306800 ( 15.1 % )
(14, 39, 64, 89) with 1 large: 472547 out of 2214000 ( 21.3 % )
(14, 39, 64, 89) with 2 large: 236765 out of 1134000 ( 20.9 % )
(14, 39, 64, 89) with 3 large: 30832 out of 198000 ( 15.6 % )
(14, 39, 64, 89) with 4 large: 825 out of 9000 ( 9.2 % )
(14, 39, 64, 89) in total: 938526 out of 4861800 ( 19.3 % )
(15, 40, 65, 90) with 0 large: 197557 out of 1306800 ( 15.1 % )
(15, 40, 65, 90) with 1 large: 454835 out of 2214000 ( 20.5 % )
(15, 40, 65, 90) with 2 large: 215742 out of 1134000 ( 19.0 % )
(15, 40, 65, 90) with 3 large: 27000 out of 198000 ( 13.6 % )
(15, 40, 65, 90) with 4 large: 715 out of 9000 ( 7.9 % )
(15, 40, 65, 90) in total: 895849 out of 4861800 ( 18.4 % )
(16, 41, 66, 91) with 0 large: 197557 out of 1306800 ( 15.1 % )
(16, 41, 66, 91) with 1 large: 472269 out of 2214000 ( 21.3 % )
(16, 41, 66, 91) with 2 large: 229466 out of 1134000 ( 20.2 % )
(16, 41, 66, 91) with 3 large: 28990 out of 198000 ( 14.6 % )
(16, 41, 66, 91) with 4 large: 747 out of 9000 ( 8.3 % )
(16, 41, 66, 91) in total: 929029 out of 4861800 ( 19.1 % )
(17, 42, 67, 92) with 0 large: 197557 out of 1306800 ( 15.1 % )
(17, 42, 67, 92) with 1 large: 476877 out of 2214000 ( 21.5 % )
(17, 42, 67, 92) with 2 large: 230190 out of 1134000 ( 20.3 % )
(17, 42, 67, 92) with 3 large: 28651 out of 198000 ( 14.5 % )
(17, 42, 67, 92) with 4 large: 733 out of 9000 ( 8.1 % )
(17, 42, 67, 92) in total: 934008 out of 4861800 ( 19.2 % )
(18, 43, 68, 93) with 0 large: 197557 out of 1306800 ( 15.1 % )
(18, 43, 68, 93) with 1 large: 471274 out of 2214000 ( 21.3 % )
(18, 43, 68, 93) with 2 large: 225795 out of 1134000 ( 19.9 % )
(18, 43, 68, 93) with 3 large: 27867 out of 198000 ( 14.1 % )
(18, 43, 68, 93) with 4 large: 701 out of 9000 ( 7.8 % )
(18, 43, 68, 93) in total: 923194 out of 4861800 ( 19.0 % )
(19, 44, 69, 94) with 0 large: 197557 out of 1306800 ( 15.1 % )
(19, 44, 69, 94) with 1 large: 481444 out of 2214000 ( 21.7 % )
(19, 44, 69, 94) with 2 large: 228012 out of 1134000 ( 20.1 % )
(19, 44, 69, 94) with 3 large: 27604 out of 198000 ( 13.9 % )
(19, 44, 69, 94) with 4 large: 675 out of 9000 ( 7.5 % )
(19, 44, 69, 94) in total: 935292 out of 4861800 ( 19.2 % )
(20, 45, 70, 95) with 0 large: 197557 out of 1306800 ( 15.1 % )
(20, 45, 70, 95) with 1 large: 455565 out of 2214000 ( 20.6 % )
(20, 45, 70, 95) with 2 large: 210153 out of 1134000 ( 18.5 % )
(20, 45, 70, 95) with 3 large: 25062 out of 198000 ( 12.7 % )
(20, 45, 70, 95) with 4 large: 615 out of 9000 ( 6.8 % )
(20, 45, 70, 95) in total: 888952 out of 4861800 ( 18.3 % )
(21, 46, 71, 96) with 0 large: 197557 out of 1306800 ( 15.1 % )
(21, 46, 71, 96) with 1 large: 468641 out of 2214000 ( 21.2 % )
(21, 46, 71, 96) with 2 large: 218959 out of 1134000 ( 19.3 % )
(21, 46, 71, 96) with 3 large: 25984 out of 198000 ( 13.1 % )
(21, 46, 71, 96) with 4 large: 605 out of 9000 ( 6.7 % )
(21, 46, 71, 96) in total: 911746 out of 4861800 ( 18.8 % )
(22, 47, 72, 97) with 0 large: 197557 out of 1306800 ( 15.1 % )
(22, 47, 72, 97) with 1 large: 472641 out of 2214000 ( 21.3 % )
(22, 47, 72, 97) with 2 large: 217650 out of 1134000 ( 19.2 % )
(22, 47, 72, 97) with 3 large: 25523 out of 198000 ( 12.9 % )
(22, 47, 72, 97) with 4 large: 587 out of 9000 ( 6.5 % )
(22, 47, 72, 97) in total: 913958 out of 4861800 ( 18.8 % )
(23, 48, 73, 98) with 0 large: 197557 out of 1306800 ( 15.1 % )
(23, 48, 73, 98) with 1 large: 473325 out of 2214000 ( 21.4 % )
(23, 48, 73, 98) with 2 large: 216440 out of 1134000 ( 19.1 % )
(23, 48, 73, 98) with 3 large: 25306 out of 198000 ( 12.8 % )
(23, 48, 73, 98) with 4 large: 581 out of 9000 ( 6.5 % )
(23, 48, 73, 98) in total: 913209 out of 4861800 ( 18.8 % )
(24, 49, 74, 99) with 0 large: 197557 out of 1306800 ( 15.1 % )
(24, 49, 74, 99) with 1 large: 462205 out of 2214000 ( 20.9 % )
(24, 49, 74, 99) with 2 large: 211736 out of 1134000 ( 18.7 % )
(24, 49, 74, 99) with 3 large: 25112 out of 198000 ( 12.7 % )
(24, 49, 74, 99) with 4 large: 585 out of 9000 ( 6.5 % )
(24, 49, 74, 99) in total: 897195 out of 4861800 ( 18.5 % )
(25, 50, 75, 100) with 0 large: 197557 out of 1306800 ( 15.1 % )
(25, 50, 75, 100) with 1 large: 461214 out of 2214000 ( 20.8 % )
(25, 50, 75, 100) with 2 large: 184916 out of 1134000 ( 16.3 % )
(25, 50, 75, 100) with 3 large: 17678 out of 198000 ( 8.9 % )
(25, 50, 75, 100) with 4 large: 400 out of 9000 ( 4.4 % )
(25, 50, 75, 100) in total: 861765 out of 4861800 ( 17.7 % )
--- 26.171717166900635 seconds ---```
