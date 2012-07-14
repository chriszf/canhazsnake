import canhazsnake

c = canhazsnake.Client("API_KEY",
        "API_SECRET")
print "Go here:"
print c.get_auth_url()
code = raw_input("Enter your access code: ")
print c.get_token(code)
print c.ohai("Test")
print c.me()
print c.site_types()
print c.my_sites()
print c.site(2)
print c.user("chriszf")
print c.asset_types()
