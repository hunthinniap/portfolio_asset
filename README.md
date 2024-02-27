Assets for my personal website at
hunthinniap.pythonanywhere.com

Folder Structure Design
specs.json is needed when something is iterable with these default attributes
└── Specs.json
├──description: {page_description}
└──Title: Subsection_name
And any src should be compiled in the backend, in case of changing the file storage

/portfolio_asset
├── main
	├── cover_photo.jpg
	├──section_photo.jpg
	└── Specs.json
├── about
	├── cover_photo.jpg
	├── description.txt
	└── journal.txt
├── section_name
├── Subsection_name.jpg (cover photo)
├── Subsection_name (folder, or file if applicable)
└── Specs.json
├──description: {page_description}
└──Title: Subsection_name
├── blog
├── blog_name.jpg (cover photo)
├── blog_name.txt
└── Specs.json
└──date: 
├── music
├── music_name.jpg (cover photo)
├── music_name
	├──lyrics.txt
└──motivation.txt
└── Specs.json
	├──description:
	├──sc_id:
└──date:
├──photography
├── photography_name.jpg 
├── photography_name
	├──photo1.jpg
	├──photo2.jpg
	└── Specs.json
├──photo_name:
		└──src:
└── Specs.json
└── videography
├── video_name.jpg 
└── Specs.json
	├──description:
	└── ytb_id:


