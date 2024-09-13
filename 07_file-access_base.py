f = open("devices.txt", "r")
routerek =[]
for router in f:
    router = router.strip()
    routerek.append(router)
    print(router.strip())
f.close()
