from torch.utils.data import Dataset



class AudioSet(Dataset):
    WINDS = ['/m/09x0r', '/m/05zppz', '/m/02zsn', '/m/0ytgt', '/m/01h8n0', '/m/02qldy', '/m/0261r1', '/m/0brhx', '/m/07p6fty', '/m/07q4ntr', '/m/07rwj3x', '/m/07sr1lc', '/m/04gy_2', '/t/dd00135', '/m/03qc9zr', '/m/02rtxlg', '/m/01j3sz', '/t/dd00001', '/m/07r660_', '/m/07s04w4', '/m/07sq110', '/m/07rgt08', '/m/0463cq4', '/t/dd00002', '/m/07qz6j3', '/m/07qw_06', '/m/07plz5l', '/m/015lz1', '/m/0l14jd', '/m/01swy6', '/m/02bk07', '/m/01c194', '/t/dd00003', '/t/dd00004', '/t/dd00005', '/t/dd00006', '/m/06bxc', '/m/02fxyj', '/m/07s2xch', '/m/07r4k75', '/m/01w250', '/m/0lyf6', '/m/07mzm6', '/m/01d3sd', '/m/07s0dtb', '/m/07pyy8b', '/m/07q0yl5', '/m/01b_21', '/m/0dl9sf8', '/m/01hsr_', '/m/07ppn3j', '/m/06h7j', '/m/07qv_x_', '/m/07pbtc8', '/m/03cczk', '/m/07pdhp0', '/m/0939n_', '/m/01g90h', '/m/03q5_w', '/m/02p3nc', '/m/02_nn', '/m/0k65p', '/m/025_jnm', '/m/0l15bq', '/m/01jg02', '/m/01jg1z', '/m/053hz1', '/m/028ght', '/m/07rkbfh', '/m/03qtwd', '/m/07qfr4h', '/t/dd00013', '/m/0jbk', '/m/068hy', '/m/0bt9lr', '/m/05tny_', '/m/07r_k2n', '/m/07qf0zm', '/m/07rc7d9', '/m/0ghcn6', '/t/dd00136', '/m/01yrx', '/m/02yds9', '/m/07qrkrw', '/m/07rjwbb', '/m/07r81j2', '/m/0ch8v', '/m/03k3r', '/m/07rv9rh', '/m/07q5rw0', '/m/01xq0k1', '/m/07rpkh9', '/m/0239kh', '/m/068zj', '/t/dd00018', '/m/03fwl', '/m/07q0h5t', '/m/07bgp', '/m/025rv6n', '/m/09b5t', '/m/07st89h', '/m/07qn5dc', '/m/01rd7k', '/m/07svc2k', '/m/09ddx', '/m/07qdb04', '/m/0dbvp', '/m/07qwf61', '/m/01280g', '/m/0cdnk', '/m/04cvmfc', '/m/015p6', '/m/020bb7', '/m/07pggtn', '/m/07sx8x_', '/m/0h0rv', '/m/07r_25d', '/m/04s8yn', '/m/07r5c2p', '/m/09d5_', '/m/07r_80w', '/m/05_wcq', '/m/01z5f', '/m/06hps', '/m/04rmv', '/m/07r4gkf', '/m/03vt0', '/m/09xqv', '/m/09f96', '/m/0h2mp', '/m/07pjwq1', '/m/01h3n', '/m/09ld4', '/m/07st88b', '/m/078jl', '/m/07qn4z3', '/m/032n05', '/m/04rlf', '/m/04szw', '/m/0fx80y', '/m/0342h', '/m/02sgy', '/m/018vs', '/m/042v_gx', '/m/06w87', '/m/01glhc', '/m/07s0s5r', '/m/018j2', '/m/0jtg0', '/m/04rzd', '/m/01bns_', '/m/07xzm', '/m/05148p4', '/m/05r5c', '/m/01s0ps', '/m/013y1f', '/m/03xq_f', '/m/03gvt', '/m/0l14qv', '/m/01v1d8', '/m/03q5t', '/m/0l14md', '/m/02hnl', '/m/0cfdd', '/m/026t6', '/m/06rvn', '/m/03t3fj', '/m/02k_mr', '/m/0bm02', '/m/011k_j', '/m/01p970', '/m/01qbl', '/m/03qtq', '/m/01sm1g', '/m/07brj', '/m/05r5wn', '/m/0xzly', '/m/0mbct', '/m/016622', '/m/0j45pbj', '/m/0dwsp', '/m/0dwtp', '/m/0dwt5', '/m/0l156b', '/m/05pd6', '/m/01kcd', '/m/0319l', '/m/07gql', '/m/07c6l', '/m/0l14_3', '/m/02qmj0d', '/m/07y_7', '/m/0d8_n', '/m/01xqw', '/m/02fsn', '/m/085jw', '/m/0l14j_', '/m/06ncr', '/m/01wy6', '/m/03m5k', '/m/0395lw', '/m/03w41f', '/m/027m70_', '/m/0gy1t2s', '/m/07n_g', '/m/0f8s22', '/m/026fgl', '/m/0150b9', '/m/03qjg', '/m/0mkg', '/m/0192l', '/m/02bxd', '/m/0l14l2', '/m/07kc_', '/m/0l14t7', '/m/01hgjl', '/m/064t9', '/m/0glt670', '/m/02cz_7', '/m/06by7', '/m/03lty', '/m/05r6t', '/m/0dls3', '/m/0dl5d', '/m/07sbbz2', '/m/05w3f', '/m/06j6l', '/m/0gywn', '/m/06cqb', '/m/01lyv', '/m/015y_n', '/m/0gg8l', '/m/02x8m', '/m/02w4v', '/m/06j64v', '/m/03_d0', '/m/026z9', '/m/0ggq0m', '/m/05lls', '/m/02lkt', '/m/03mb9', '/m/07gxw', '/m/07s72n', '/m/0283d', '/m/0m0jc', '/m/08cyft', '/m/0fd3y', '/m/07lnk', '/m/0g293', '/m/0ln16', '/m/0326g', '/m/0155w', '/m/05fw6t', '/m/02v2lh', '/m/0y4f8', '/m/0z9c', '/m/0164x2', '/m/0145m', '/m/02mscn', '/m/016cjb', '/m/028sqc', '/m/015vgc', '/m/0dq0md', '/m/06rqw', '/m/02p0sh1', '/m/05rwpb',
         '/m/074ft', '/m/025td0t', '/m/02cjck', '/m/03r5q_', '/m/0l14gg', '/m/07pkxdp', '/m/01z7dr', '/m/0140xf', '/m/0ggx5q', '/m/04wptg', '/t/dd00031', '/t/dd00032', '/t/dd00033', '/t/dd00034', '/t/dd00035', '/t/dd00036', '/t/dd00037', '/m/03m9d0z', '/m/09t49', '/t/dd00092', '/m/0jb2l', '/m/0ngt1', '/m/0838f', '/m/06mb1', '/m/07r10fb', '/t/dd00038', '/m/0j6m2', '/m/0j2kx', '/m/05kq4', '/m/034srq', '/m/06wzb', '/m/07swgks', '/m/02_41', '/m/07pzfmf', '/m/07yv9', '/m/019jd', '/m/0hsrw', '/m/056ks2', '/m/02rlv9', '/m/06q74', '/m/012f08', '/m/0k4j', '/m/0912c9', '/m/07qv_d5', '/m/02mfyn', '/m/04gxbd', '/m/07rknqz', '/m/0h9mv', '/t/dd00134', '/m/0ltv', '/m/07r04', '/m/0gvgw0', '/m/05x_td', '/m/02rhddq', '/m/03cl9h', '/m/01bjv', '/m/03j1ly', '/m/04qvtq', '/m/012n7d', '/m/012ndj', '/m/04_sv', '/m/0btp2', '/m/06d_3', '/m/07jdr', '/m/04zmvq', '/m/0284vy3', '/m/01g50p', '/t/dd00048', '/m/0195fx', '/m/0k5j', '/m/014yck', '/m/04229', '/m/02l6bg', '/m/09ct_', '/m/0cmf2', '/m/0199g', '/m/06_fw', '/m/02mk9', '/t/dd00065', '/m/08j51y', '/m/01yg9g', '/m/01j4z9', '/t/dd00066', '/t/dd00067', '/m/01h82_', '/t/dd00130', '/m/07pb8fc', '/m/07q2z82', '/m/02dgv', '/m/03wwcy', '/m/07r67yg', '/m/02y_763', '/m/07rjzl8', '/m/07r4wb8', '/m/07qcpgn', '/m/07q6cd_', '/m/0642b4', '/m/0fqfqc', '/m/04brg2', '/m/023pjk', '/m/07pn_8q', '/m/0dxrf', '/m/0fx9l', '/m/02pjr4', '/m/02jz0l', '/m/0130jx', '/m/03dnzn', '/m/03wvsk', '/m/01jt3m', '/m/012xff', '/m/04fgwm', '/m/0d31p', '/m/01s0vc', '/m/03v3yw', '/m/0242l', '/m/01lsmm', '/m/02g901', '/m/05rj2', '/m/0316dw', '/m/0c2wf', '/m/01m2v', '/m/081rb', '/m/07pp_mv', '/m/07cx4', '/m/07pp8cl', '/m/01hnzm', '/m/02c8p', '/m/015jpf', '/m/01z47d', '/m/046dlr', '/m/03kmc9', '/m/0dgbq', '/m/030rvx', '/m/01y3hg', '/m/0c3f7m', '/m/04fq5q', '/m/0l156k', '/m/06hck5', '/t/dd00077', '/m/02bm9n', '/m/01x3z', '/m/07qjznt', '/m/07qjznl', '/m/0l7xg', '/m/05zc1', '/m/0llzx', '/m/02x984l', '/m/025wky1', '/m/024dl', '/m/01m4t', '/m/0dv5r', '/m/07bjf', '/m/07k1x', '/m/03l9g', '/m/03p19w', '/m/01b82r', '/m/02p01q', '/m/023vsd', '/m/0_ksk', '/m/01d380', '/m/014zdl', '/m/032s66', '/m/04zjc', '/m/02z32qm', '/m/0_1c', '/m/073cg4', '/m/0g6b5', '/g/122z_qxw', '/m/07qsvvw', '/m/07pxg6y', '/m/07qqyl4', '/m/083vt', '/m/07pczhz', '/m/07pl1bw', '/m/07qs1cx', '/m/039jq', '/m/07q7njn', '/m/07rn7sz', '/m/04k94', '/m/07rrlb6', '/m/07p6mqd', '/m/07qlwh6', '/m/07r5v4s', '/m/07prgkl', '/m/07pqc89', '/t/dd00088', '/m/07p7b8y', '/m/07qlf79', '/m/07ptzwd', '/m/07ptfmf', '/m/0dv3j', '/m/0790c', '/m/0dl83', '/m/07rqsjt', '/m/07qnq_y', '/m/07rrh0c', '/m/0b_fwt', '/m/02rr_', '/m/07m2kt', '/m/018w8', '/m/07pws3f', '/m/07ryjzk', '/m/07rdhzs', '/m/07pjjrj', '/m/07pc8lb', '/m/07pqn27', '/m/07rbp7_', '/m/07pyf11', '/m/07qb_dv', '/m/07qv4k0', '/m/07pdjhy', '/m/07s8j8t', '/m/07plct2', '/t/dd00112', '/m/07qcx4z', '/m/02fs_r', '/m/07qwdck', '/m/07phxs1', '/m/07rv4dm', '/m/07s02z0', '/m/07qh7jl', '/m/07qwyj0', '/m/07s34ls', '/m/07qmpdm', '/m/07p9k1k', '/m/07qc9xj', '/m/07rwm0c', '/m/07phhsh', '/m/07qyrcz', '/m/07qfgpx', '/m/07rcgpl', '/m/07p78v5', '/t/dd00121', '/m/07s12q4', '/m/028v0c', '/m/01v_m0', '/m/0b9m1', '/m/0hdsk', '/m/0c1dj', '/m/07pt_g0', '/t/dd00125', '/t/dd00126', '/t/dd00127', '/t/dd00128', '/t/dd00129', '/m/01b9nn', '/m/01jnbd', '/m/096m7z', '/m/06_y0by', '/m/07rgkc5', '/m/06xkwv', '/m/0g12c5', '/m/08p9q4', '/m/07szfh9', '/m/0chx_', '/m/0cj0r', '/m/07p_0gm', '/m/01jwx6', '/m/07c52', '/m/06bz3', '/m/07hvw1']

    CLASSES = ['Speech', 'Male speech, man speaking', 'Female speech, woman speaking', 'Child speech, kid speaking', 'Conversation', 'Narration, monologue', 'Babbling', 'Speech synthesizer', 'Shout', 'Bellow', 'Whoop', 'Yell', 'Battle cry', 'Children shouting', 'Screaming', 'Whispering', 'Laughter', 'Baby laughter', 'Giggle', 'Snicker', 'Belly laugh', 'Chuckle, chortle', 'Crying, sobbing', 'Baby cry, infant cry', 'Whimper', 'Wail, moan', 'Sigh', 'Singing', 'Choir', 'Yodeling', 'Chant', 'Mantra', 'Male singing', 'Female singing', 'Child singing', 'Synthetic singing', 'Rapping', 'Humming', 'Groan', 'Grunt', 'Whistling', 'Breathing', 'Wheeze', 'Snoring', 'Gasp', 'Pant', 'Snort', 'Cough', 'Throat clearing', 'Sneeze', 'Sniff', 'Run', 'Shuffle', 'Walk, footsteps', 'Chewing, mastication', 'Biting', 'Gargling', 'Stomach rumble', 'Burping, eructation', 'Hiccup', 'Fart', 'Hands', 'Finger snapping', 'Clapping', 'Heart sounds, heartbeat', 'Heart murmur', 'Cheering', 'Applause', 'Chatter', 'Crowd', 'Hubbub, speech noise, speech babble', 'Children playing', 'Animal', 'Domestic animals, pets', 'Dog', 'Bark', 'Yip', 'Howl', 'Bow-wow', 'Growling', 'Whimper (dog)', 'Cat', 'Purr', 'Meow', 'Hiss', 'Caterwaul', 'Livestock, farm animals, working animals', 'Horse', 'Clip-clop', 'Neigh, whinny', 'Cattle, bovinae', 'Moo', 'Cowbell', 'Pig', 'Oink', 'Goat', 'Bleat', 'Sheep', 'Fowl', 'Chicken, rooster', 'Cluck', 'Crowing, cock-a-doodle-doo', 'Turkey', 'Gobble', 'Duck', 'Quack', 'Goose', 'Honk', 'Wild animals', 'Roaring cats (lions, tigers)', 'Roar', 'Bird', 'Bird vocalization, bird call, bird song', 'Chirp, tweet', 'Squawk', 'Pigeon, dove', 'Coo', 'Crow', 'Caw', 'Owl', 'Hoot', 'Bird flight, flapping wings', 'Canidae, dogs, wolves', 'Rodents, rats, mice', 'Mouse', 'Patter', 'Insect', 'Cricket', 'Mosquito', 'Fly, housefly', 'Buzz', 'Bee, wasp, etc.', 'Frog', 'Croak', 'Snake', 'Rattle', 'Whale vocalization', 'Music', 'Musical instrument', 'Plucked string instrument', 'Guitar', 'Electric guitar', 'Bass guitar', 'Acoustic guitar', 'Steel guitar, slide guitar', 'Tapping (guitar technique)', 'Strum', 'Banjo', 'Sitar', 'Mandolin', 'Zither', 'Ukulele', 'Keyboard (musical)', 'Piano', 'Electric piano', 'Organ', 'Electronic organ', 'Hammond organ', 'Synthesizer', 'Sampler', 'Harpsichord', 'Percussion', 'Drum kit', 'Drum machine', 'Drum', 'Snare drum', 'Rimshot', 'Drum roll', 'Bass drum', 'Timpani', 'Tabla', 'Cymbal', 'Hi-hat', 'Wood block', 'Tambourine', 'Rattle (instrument)', 'Maraca', 'Gong', 'Tubular bells', 'Mallet percussion', 'Marimba, xylophone', 'Glockenspiel', 'Vibraphone', 'Steelpan', 'Orchestra', 'Brass instrument', 'French horn', 'Trumpet', 'Trombone', 'Bowed string instrument', 'String section', 'Violin, fiddle', 'Pizzicato', 'Cello', 'Double bass', 'Wind instrument, woodwind instrument', 'Flute', 'Saxophone', 'Clarinet', 'Harp', 'Bell', 'Church bell', 'Jingle bell', 'Bicycle bell', 'Tuning fork', 'Chime', 'Wind chime', 'Change ringing (campanology)', 'Harmonica', 'Accordion', 'Bagpipes', 'Didgeridoo', 'Shofar', 'Theremin', 'Singing bowl', 'Scratching (performance technique)', 'Pop music', 'Hip hop music', 'Beatboxing', 'Rock music', 'Heavy metal', 'Punk rock', 'Grunge', 'Progressive rock', 'Rock and roll', 'Psychedelic rock', 'Rhythm and blues', 'Soul music', 'Reggae', 'Country', 'Swing music', 'Bluegrass', 'Funk', 'Folk music', 'Middle Eastern music', 'Jazz', 'Disco', 'Classical music', 'Opera', 'Electronic music', 'House music', 'Techno', 'Dubstep', 'Drum and bass', 'Electronica', 'Electronic dance music', 'Ambient music', 'Trance music', 'Music of Latin America', 'Salsa music', 'Flamenco', 'Blues', 'Music for children', 'New-age music', 'Vocal music', 'A capella', 'Music of Africa', 'Afrobeat', 'Christian music', 'Gospel music', 'Music of Asia', 'Carnatic music', 'Music of Bollywood', 'Ska', 'Traditional music', 'Independent music', 'Song', 'Background music', 'Theme music', 'Jingle (music)', 'Soundtrack music', 'Lullaby',
            'Video game music', 'Christmas music', 'Dance music', 'Wedding music', 'Happy music', 'Funny music', 'Sad music', 'Tender music', 'Exciting music', 'Angry music', 'Scary music', 'Wind', 'Rustling leaves', 'Wind noise (microphone)', 'Thunderstorm', 'Thunder', 'Water', 'Rain', 'Raindrop', 'Rain on surface', 'Stream', 'Waterfall', 'Ocean', 'Waves, surf', 'Steam', 'Gurgling', 'Fire', 'Crackle', 'Vehicle', 'Boat, Water vehicle', 'Sailboat, sailing ship', 'Rowboat, canoe, kayak', 'Motorboat, speedboat', 'Ship', 'Motor vehicle (road)', 'Car', 'Vehicle horn, car horn, honking', 'Toot', 'Car alarm', 'Power windows, electric windows', 'Skidding', 'Tire squeal', 'Car passing by', 'Race car, auto racing', 'Truck', 'Air brake', 'Air horn, truck horn', 'Reversing beeps', 'Ice cream truck, ice cream van', 'Bus', 'Emergency vehicle', 'Police car (siren)', 'Ambulance (siren)', 'Fire engine, fire truck (siren)', 'Motorcycle', 'Traffic noise, roadway noise', 'Rail transport', 'Train', 'Train whistle', 'Train horn', 'Railroad car, train wagon', 'Train wheels squealing', 'Subway, metro, underground', 'Aircraft', 'Aircraft engine', 'Jet engine', 'Propeller, airscrew', 'Helicopter', 'Fixed-wing aircraft, airplane', 'Bicycle', 'Skateboard', 'Engine', 'Light engine (high frequency)', "Dental drill, dentist's drill", 'Lawn mower', 'Chainsaw', 'Medium engine (mid frequency)', 'Heavy engine (low frequency)', 'Engine knocking', 'Engine starting', 'Idling', 'Accelerating, revving, vroom', 'Door', 'Doorbell', 'Ding-dong', 'Sliding door', 'Slam', 'Knock', 'Tap', 'Squeak', 'Cupboard open or close', 'Drawer open or close', 'Dishes, pots, and pans', 'Cutlery, silverware', 'Chopping (food)', 'Frying (food)', 'Microwave oven', 'Blender', 'Water tap, faucet', 'Sink (filling or washing)', 'Bathtub (filling or washing)', 'Hair dryer', 'Toilet flush', 'Toothbrush', 'Electric toothbrush', 'Vacuum cleaner', 'Zipper (clothing)', 'Keys jangling', 'Coin (dropping)', 'Scissors', 'Electric shaver, electric razor', 'Shuffling cards', 'Typing', 'Typewriter', 'Computer keyboard', 'Writing', 'Alarm', 'Telephone', 'Telephone bell ringing', 'Ringtone', 'Telephone dialing, DTMF', 'Dial tone', 'Busy signal', 'Alarm clock', 'Siren', 'Civil defense siren', 'Buzzer', 'Smoke detector, smoke alarm', 'Fire alarm', 'Foghorn', 'Whistle', 'Steam whistle', 'Mechanisms', 'Ratchet, pawl', 'Clock', 'Tick', 'Tick-tock', 'Gears', 'Pulleys', 'Sewing machine', 'Mechanical fan', 'Air conditioning', 'Cash register', 'Printer', 'Camera', 'Single-lens reflex camera', 'Tools', 'Hammer', 'Jackhammer', 'Sawing', 'Filing (rasp)', 'Sanding', 'Power tool', 'Drill', 'Explosion', 'Gunshot, gunfire', 'Machine gun', 'Fusillade', 'Artillery fire', 'Cap gun', 'Fireworks', 'Firecracker', 'Burst, pop', 'Eruption', 'Boom', 'Wood', 'Chop', 'Splinter', 'Crack', 'Glass', 'Chink, clink', 'Shatter', 'Liquid', 'Splash, splatter', 'Slosh', 'Squish', 'Drip', 'Pour', 'Trickle, dribble', 'Gush', 'Fill (with liquid)', 'Spray', 'Pump (liquid)', 'Stir', 'Boiling', 'Sonar', 'Arrow', 'Whoosh, swoosh, swish', 'Thump, thud', 'Thunk', 'Electronic tuner', 'Effects unit', 'Chorus effect', 'Basketball bounce', 'Bang', 'Slap, smack', 'Whack, thwack', 'Smash, crash', 'Breaking', 'Bouncing', 'Whip', 'Flap', 'Scratch', 'Scrape', 'Rub', 'Roll', 'Crushing', 'Crumpling, crinkling', 'Tearing', 'Beep, bleep', 'Ping', 'Ding', 'Clang', 'Squeal', 'Creak', 'Rustle', 'Whir', 'Clatter', 'Sizzle', 'Clicking', 'Clickety-clack', 'Rumble', 'Plop', 'Jingle, tinkle', 'Hum', 'Zing', 'Boing', 'Crunch', 'Silence', 'Sine wave', 'Harmonic', 'Chirp tone', 'Sound effect', 'Pulse', 'Inside, small room', 'Inside, large room or hall', 'Inside, public space', 'Outside, urban or manmade', 'Outside, rural or natural', 'Reverberation', 'Echo', 'Noise', 'Environmental noise', 'Static', 'Mains hum', 'Distortion', 'Sidetone', 'Cacophony', 'White noise', 'Pink noise', 'Throbbing', 'Vibration', 'Television', 'Radio', 'Field recording']

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()