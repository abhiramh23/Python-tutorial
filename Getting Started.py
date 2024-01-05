# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: hydrogen
#       format_version: '1.3'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # INTRODUCTION
#   * Python is high level language, general purpose, simple syntax, very large library  
#   * Indentation is important in this language (*4 space default*)  
#   * Developed in the 1980's by Guido van Rossum.  
#    
#    it can be install in 
#    ## LINUX
#       For linux there are two ways 
#    1. using package manager like apt , pacman , dnf , yum, etc 
#    2. using source file form github or any other platform to build 
#    ## MAC OS
#     For mac os using brew package manger
#    ## WINDOWS
#      For windows there are two ways
#    1. using package manager like **winget** , chocolaty , scoop
#    2. using executive file (**exe**) installer  

# %% [markdown]
# ### Print Statement

# %%
print("Hello World \n")


# %% [markdown]
# ### Basic operations

# %%
sum = 21 + 54
print(sum)


# %%
difference = 54 - 78
print(difference)


# %%
product = 13 * 54
print(product)


# %%
modulus = 45 % 7
print(modulus)


# %%
quotient = 45 / 7
print(quotient)


# %%
onlyintdoubleslash = 45 // 7
print(onlyintdoubleslash)


# %%
power = 2**2
print(power)


# %% [markdown]
# ### Conversion

# %% [markdown]
# `str()` is a keyword which convert any data type to string

# %%
str(127768.7876)


# %% [markdown]
# `int()` is a keyword which convert any data type to integer

# %%
int(21293323.23232321)


# %% [markdown]
# `type()` is a keyword which tells us which data type 

# %%
type(23223.3323)


# %% [markdown]
# ### Complex Numbers

# %%
a = 5 + 3j
type(a)


# %%
print(a)


# %%
a.imag


# %%
a.real

