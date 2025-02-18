set parentImageFile to ""

-- Retrieve the current image selected in Capture One
tell application "Capture One 12"
	repeat with variantItem in (get selected variants)
		set parentImageFile to (get path of (get parent image of variantItem))
		if (parentImageFile is not equal to "") then exit repeat
	end repeat
end tell

if (parentImageFile is equal to "") then
	display dialog "No path found. Did you select an image?"
	return
end if

-- Get the path to the image
set parentImagePath to (parentFolderOf for parentImageFile)

-- Call the python script
set commandLine to "eval `/usr/libexec/path_helper -s`; python3 -m geocode"
set commandLine to (commandLine & " \"" & parentImagePath & "/*.xmp\"")

display dialog commandLine
do shell script commandLine

-- Notify the user
display notification "Images successfully geocoded"

-- From: https://stackoverflow.com/questions/30823900/getting-directory-of-input-file-applescript
to parentFolderOf for pxPath
	-- Assumes no superfluous slashes
	set {tids, text item delimiters, i} to {text item delimiters, "/", ((pxPath ends with "/") as integer) + 1}
	set {parFol, text item delimiters} to {text 1 thru text item -(i + 1) of pxPath, tids}
	return parFol
end parentFolderOf
