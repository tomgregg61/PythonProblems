maxNetBandwidthMbps = 1000
noConcurrentUsers = 200
appAReqBps = 200000
appBReqBps = 100000
appNewReqBps = 350000

maxNetBandwidthBps = maxNetBandwidthMbps * 1000000
currentUsage = (appAReqBps * noConcurrentUsers) + (appBReqBps * noConcurrentUsers)
currentAvailability = maxNetBandwidthBps - currentUsage
availableBandwidthAfter = round((maxNetBandwidthBps - currentUsage - (appNewReqBps * noConcurrentUsers)) / 1000000)

print("Network in capacity in bps:", maxNetBandwidthBps)
print("Current usage in bps:", currentUsage)
print("Current availability:", currentAvailability)
print("New application's requirements in bps:", appNewReqBps)
print("Bandwidth available if new application is installed in Mbps", availableBandwidthAfter) 