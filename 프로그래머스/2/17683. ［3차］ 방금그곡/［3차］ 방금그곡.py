import re

def solution(m, musicinfos):
    answer = ''
    s = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a', 'B#':'b'}
    song = {}

    for f in (re.findall('[C, D, F, G, A, B]#', m)):
        m = m.replace(f, s[f])

    for i, v in enumerate(musicinfos):
        start, end, name, melody = v.split(',')

        for f in (re.findall('[C, D, F, G, A, B]#', melody)):
            melody = melody.replace(f, s[f])

        song_length = len(melody)

        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        song_time = ((end_h * 60) + end_m) - ((start_h * 60) + start_m)

        div, mod = divmod(song_time, song_length)
        total_melody = (melody * div) + melody[:mod]

        if(m in total_melody):
            song[name] = [song_time, melody, i]

    if(len(song) == 0):
        return "(None)"
    else:
        return sorted(song.items(), key = lambda x: (-x[1][0], x[1][2]))[0][0]