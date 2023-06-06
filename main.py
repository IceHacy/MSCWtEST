import pygame, ntplib

from datetime import datetime

import pytz

# Initialize Pygame

pygame.init()

# Set the window dimensions and create a Pygame clock

WINDOW_SIZE = (400, 200)

screen = pygame.display.set_mode(WINDOW_SIZE)

pygame.display.set_caption('Time Zones')

clock = pygame.time.Clock()

# Set the font and font size

FONT_SIZE = 30

fnt = pygame.font.SysFont('Arial', FONT_SIZE)

# Set the Moscow timezone as default

moscow_now = ''

est_now = ''

TZ_1 = pytz.timezone('Europe/Moscow')

TZ_2 = pytz.timezone('US/Eastern')

# Set the time difference between local and UTC time

ntp_client = ntplib.NTPClient()

response = ntp_client.request('pool.ntp.org', version=3)

LOCAL_DIFF = datetime.now() - datetime.fromtimestamp(response.tx_time)

# Set some example holidays

holidays = {

    '01-01': 'New Year\'s Day',

    '02-14': 'Valentine\'s Day',

    '04-01': 'April Fools\' Day',

    '12-25': 'Christmas Day',

    '12-31': 'New Year\'s Eve'

}

# Start the clock loop

while True:

    # Handle Pygame events

    for event in pygame.event.get():

        if event.type == pygame.QUIT:

            pygame.quit()

            quit()

    # Get the local time and update the display clock

    moscow_now = datetime.now(TZ_1) + LOCAL_DIFF

    est_now = datetime.now(TZ_2) + LOCAL_DIFF

    # Get the current day and format it

    moscow_day = moscow_now.strftime('%A')

    est_day = est_now.strftime('%A')

    # Get the current date and format it

    moscow_date = moscow_now.strftime('%B %d')

    est_date = est_now.strftime('%B %d')

    # Check if today is a holiday and display it if it is

    moscow_holiday = holidays.get(moscow_now.strftime('%m-%d'), '')

    est_holiday = holidays.get(est_now.strftime('%m-%d'), '')

    # Render the clocks and dates

    moscow_text = fnt.render('Moscow Time: ' + moscow_day + ', ' + moscow_date + moscow_now.strftime(' %H:%M:%S'), True, (255, 255, 255))

    est_text = fnt.render('EST Time: ' + est_day + ', ' + est_date + est_now.strftime(' %H:%M:%S'), True, (255, 255, 255))

    # Render holiday message if today is a holiday

    if moscow_holiday:

        moscow_holiday_text = fnt.render('Holiday in Moscow: ' + moscow_holiday, True, (255, 255, 0))

        screen.blit(moscow_holiday_text, (20, 120))

    if est_holiday:

        est_holiday_text = fnt.render('Holiday in EST: ' + est_holiday, True, (255, 255, 0))

        screen.blit(est_holiday_text, (20, 160))

    # Clear the screen and render the displayed clock and date

    screen.fill((0, 0, 0))

    screen.blit(moscow_text, (20, 20))

    screen.blit(est_text, (20, 70))

    # Update the Pygame display

    pygame.display.update()

    # Set the Pygame clock to update at 1 frame per second (FPS)

    clock.tick(1)
