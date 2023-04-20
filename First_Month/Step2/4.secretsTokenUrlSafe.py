import secrets
passwordResetLink = "https://khine.com/python/reset="
passwordResetLink+=secrets.token_urlsafe(32)#32 bytes #2015
print('Generating secure URL: ',passwordResetLink)