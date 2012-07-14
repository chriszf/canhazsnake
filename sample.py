import canhazsnake

c = canhazsnake.Client("473cdb8554878829ce497183dd7e0a0a",
        "4e6881a0897ad0e7148a9d1817563576")
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
