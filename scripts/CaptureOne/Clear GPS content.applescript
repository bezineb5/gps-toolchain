display dialog "This will clear the content of the GPS. Are you sure?" default button "Cancel"
display dialog "Just to confirm: this will clear the content of the GPS. Are you sure?" default button "Cancel"

do shell script "eval `/usr/libexec/path_helper -s`; python3 -m gt2gpx --usb purge"

-- Notify the user
display notification "GPS device cleared"
