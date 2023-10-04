#Crab tho

import time, sys
indent = 0
indentIncreasing = True

print("It's")
time.sleep(0.5)
print('Time')
time.sleep(0.5)
print('For')
time.sleep(0.5)
print('A')
time.sleep(0.5)
print('Crab')
time.sleep(0.5)
print('Party')
time.sleep(1)


try:
  while True:
    print('   ' * indent, end='')
    print('░░▄█▀▀▀░░░░░░░░▀▀▀█▄')
    print('   ' * indent, end='')
    print('▄███▄▄░░▀▄██▄▀░░▄▄███▄')
    print('   ' * indent, end='')
    print('▀██▄▄▄▄████████▄▄▄▄██▀')
    print('   ' * indent, end='')
    print('░░▄▄▄▄██████████▄▄▄▄')
    print('   ' * indent, end='')
    print('░▐▐▀▐▀░▀██████▀░▀▌▀▌▌')
    print('   ' * indent, end='')
    print('                    ')
    time.sleep(0.3)

    if indentIncreasing:
      indent += 1
      if indent == 10:
        print("Back to the left!")
        indentIncreasing = False
    else:
      indent -= 1
      if indent == 0:
        print('                                            Back to the right!')
        indentIncreasing = True
except KeyboardInterrupt:
  sys.exit()