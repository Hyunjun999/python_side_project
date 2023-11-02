import itertools

# itertools supports various functions can be used in set theory or probability such as
# cartesian product, combinations, permutations, and combinations_with_replacement
import zipfile

# In unix or linux systemm you can make a zip file with a specific password through a terminal with 'zip -er' command and options.
# I set the password of project_06.zip as '1234'


def un_zip(pw_str, min_len, max_len, zip):
    for i in range(min_len, max_len + 1):
        attempt = itertools.product(pw_str, repeat=i)
        for a in attempt:
            pw = "".join(a)
            print(pw)
            try:
                zip.extractall(pwd=pw.encode())
                print(f"Zip file password is: {pw}")
                return  # Here, by returning some value or none inside the function,
            # we can terminate the whole process what we cannot do this just using 'break'
            except:
                pass


pw_str = (
    "".join([str(i) for i in range(0, 10)])
    + "abcdefghijklmnopqrstuvwxyz"
    + "abcdefghijklmnopqrstuvwxyz".upper()
)  # password is a alpha-numeric value and also case-sensitive
zfile = zipfile.ZipFile(r"project_06.zip")
min_l, max_l = 1, 5

pw = un_zip(pw_str, min_l, max_l, zfile)
