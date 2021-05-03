import time
from python_get_resolve import GetResolve


def timecode_from_frame(frame, fps=24, offset=0):
    return time.strftime("01:%M:%S:00", time.gmtime((frame + offset) / fps))


resolve = app.GetResolve()

projectManager = resolve.GetProjectManager()
project = projectManager.GetCurrentProject()
clip = project.GetCurrentTimeline().GetCurrentVideoItem()
currentTimeline = project.GetCurrentTimeline()
offset = currentTimeline.GetStartFrame()
markersList = currentTimeline.GetMarkers()

mediaPool = project.GetMediaPool()
rootFolder = mediaPool.GetRootFolder()
clips = rootFolder.GetClipList()

if not markersList:
    print('No Markers found!')
    sys.exit(0)

sorted_marker_keys = sorted(markersList.keys())

keys_file_names = list(
    map(lambda k: (k, 'img-%s.png' % markersList[k]['name']), sorted_marker_keys))

for frame, filename in keys_file_names:
    for clip in clips:
        if(clip.GetName() == filename):
            tc = timecode_from_frame(frame)
            tc2 = timecode_from_frame(frame, offset=96)
            # print(filename, tc, tc2)
            clip.SetClipProperty('Start TC', tc)
            clip.SetClipProperty('End TC', tc2)

sys.exit(0)
