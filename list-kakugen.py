﻿import random

kakugen = [
	"能ある鷹は爪を隠す"
	"豚に真珠"
	"二兎追うものは一兎も得ず"
	"叩き続けなさい。そうすれば開かれます"]

i = random.randint(0, len(kakugen)-1)

print( kakugen[i] )