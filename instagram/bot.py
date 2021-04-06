from asyncio import sleep, run
from instapy_cli import client

from main.logs import Console
from resources_manager.config import get_config, Keys
from resources_manager.database import is_story_saved, write_story
from resources_manager.directory import save_file


console = Console('Insta bot')


async def main():
    with client(get_config(Keys.InstagramUsername), get_config(Keys.InstagramPassword)) as clt:
        console.start()
        while True:
            user = 'Liza_3918'
            console.new_insta_loop(user)

            stories = get_stories(clt, user)
            download_stories(stories, user)

            await sleep(600)


def get_stories(clt: client, user: str) -> list:
    user = clt.client.username_info(user)
    stories_soup = clt.client.user_story_feed(user['user']['pk'])['reel']['items']

    return [(story['pk'], 'mp4', story['video_versions'][0]['url']) if 'video_versions' in story.keys()
            else (story['pk'], 'jpg', story['image_versions2']['candidates'][-1]['url']) for story in stories_soup]


def download_stories(stories: list, user: str):
    for (story_id, story_type, story) in stories:
        if not is_story_saved(story_id):
            save_file(story, story_id, story_type)
            write_story(story_id, user)

            console.story_was_saved(user)


if __name__ == '__main__':
    run(main())
