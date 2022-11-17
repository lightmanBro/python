def cels_from_fahr(fahr):
          cels = (fahr - 32) * 5/9
          return cels

if __name__ == '__name__':
    res = cels_from_fahr(5)
    print(res)