import speedtest

st = speedtest.Speedtest()

def bytestombps(value):
    kb = 1024
    mb = kb ** 2
    return value / mb

downspeed = st.download()
upspeed = st.upload()
ping = st.results.ping

print(f"Download speed: {bytestombps(downspeed)} Mbps")
print(f"Upload speed: {bytestombps(upspeed)} Mbps")
print(f"Ping: {ping} ms")