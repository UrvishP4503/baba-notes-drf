function fetchNotes() {
  let temp = [
    {
      title: "Lorem Ipsum 1",
      noteText:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
      created_at: "2024-01-30 12:45:30",
    },
    {
      title: "Lorem Ipsum 2",
      noteText:
        "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
      created_at: "2024-01-29 10:30:15",
    },
    {
      title: "Lorem Ipsum 3",
      noteText:
        "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
      created_at: "2024-01-28 08:20:45",
    },
    {
      title: "Lorem Ipsum 4",
      noteText:
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
      created_at: "2024-01-27 18:10:08",
    },
    {
      title: "Lorem Ipsum 5",
      noteText:
        "Curabitur pretium tincidunt lacus. Nulla gravida orci a odio. Nullam varius, turpis et commodo pharetra.",
      created_at: "2024-01-26 09:40:55",
    },
    {
      title: "Lorem Ipsum 6",
      noteText:
        "Maecenas accumsan mauris sed lacus tincidunt elementum. Duis cursus, mi quis viverra ornare.",
      created_at: "2024-01-25 16:20:30",
    },
    {
      title: "Lorem Ipsum 7",
      noteText:
        "Suspendisse ac convallis urna, vitae pulvinar augue. Pellentesque vehicula efficitur tortor, vel feugiat neque.",
      created_at: "2024-01-24 22:15:12",
    },
    {
      title: "Lorem Ipsum 8",
      noteText:
        "Vestibulum vel quam id urna lobortis luctus. Nullam in quam a turpis bibendum aliquet.",
      created_at: "2024-01-23 14:05:40",
    },
    {
      title: "Lorem Ipsum 9",
      noteText:
        "Proin sed metus vel velit luctus egestas. Aliquam sagittis justo nec lectus molestie, vitae fringilla erat convallis.",
      created_at: "2024-01-22 11:30:18",
    },
    {
      title: "Lorem Ipsum 10",
      noteText:
        "Integer rhoncus mi eu massa tincidunt, sit amet sollicitudin justo dictum. Fusce interdum eget libero id dapibus.",
      created_at: "2024-01-21 07:45:55",
    },
    {
      title: "Lorem Ipsum 11",
      noteText:
        "Quisque eu est accumsan, tristique libero ut, cursus nulla. Nunc lacinia augue non dui fringilla, nec viverra ligula semper.",
      created_at: "2024-01-20 15:10:32",
    },
    {
      title: "Lorem Ipsum 12",
      noteText:
        "Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas.",
      created_at: "2024-01-19 19:25:20",
    },
    {
      title: "Lorem Ipsum 13",
      noteText:
        "Nam ultricies velit vel leo faucibus, vel tristique dui auctor. Sed ac risus ut metus volutpat fermentum nec vel justo.",
      created_at: "2024-01-18 12:55:48",
    },
    {
      title: "Lorem Ipsum 14",
      noteText:
        "Phasellus vulputate odio eu metus tristique, vel fringilla nunc feugiat. Sed vitae odio et tellus convallis luctus.",
      created_at: "2024-01-17 08:30:25",
    },
    {
      title: "Lorem Ipsum 15",
      noteText:
        "Nunc finibus sem in mi sollicitudin, a malesuada neque aliquet. Etiam commodo arcu sit amet efficitur varius.",
      created_at: "2024-01-16 14:15:10",
    },
    {
      title: "Lorem Ipsum 16",
      noteText:
        "Donec aliquet metus at justo dictum, eget vulputate eros ullamcorper. Sed nec massa ut nunc venenatis eleifend.",
      created_at: "2024-01-15 21:20:40",
    },
    {
      title: "Lorem Ipsum 17",
      noteText:
        "Fusce vitae nisi ac tortor fermentum bibendum nec ac ex. Suspendisse vitae justo vel elit scelerisque volutpat.",
      created_at: "2024-01-14 17:40:15",
    },
    {
      title: "Lorem Ipsum 18",
      noteText:
        "Praesent nec elit et nunc consectetur vulputate. Sed eu magna eget justo iaculis tristique a a felis.",
      created_at: "2024-01-13 09:55:32",
    },
    {
      title: "Lorem Ipsum 19",
      noteText:
        "Vivamus dapibus lacus id risus consectetur, in bibendum purus gravida. Nam in malesuada elit.",
      created_at: "2024-01-12 14:30:20",
    },
    {
      title: "Lorem Ipsum 20",
      noteText:
        "In sed sapien sit amet purus auctor elementum. Sed vel odio at est feugiat bibendum vitae eu ex.",
      created_at: "2024-01-11 19:25:48",
    },
    {
      title: "Lorem Ipsum 21",
      noteText:
        "Curabitur dictum sapien id neque fermentum, nec dignissim ligula eleifend. Fusce vitae lectus sit amet nulla dignissim consectetur.",
      created_at: "2024-01-10 11:50:25",
    },
    {
      title: "Lorem Ipsum 22",
      noteText:
        "Mauris nec nulla nec justo consequat aliquam at vel quam. Praesent vehicula, nisi ut euismod egestas, tortor elit hendrerit justo.",
      created_at: "2024-01-09 07:35:10",
    },
    {
      title: "Lorem Ipsum 25",
      noteText:
        "Sunt in culpa qui officia deserunt mollit anim id est laborum.",
      created_at: "2024-01-15 14:55:22",
    },
  ];

  temp.map(data => {
    if (data.noteText.length >= 105) {
      data.noteText = data.noteText.substring(0, 97) + "...";
    }
  });

  return temp;
}

export default fetchNotes;
