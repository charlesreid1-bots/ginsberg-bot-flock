import markdown

AUTHOR = 'charlesreid1'
SITENAME = 'ginsberg bot flock'
SITEURL = 'b-ginsberg'
PATH = 'content'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'

# --------------8<---------------------

THEME = 'scurvy-knave-theme'

LICENSE_URL = "https://opensource.org/licenses/MIT"
LICENSE_NAME = "MIT License"

# Pelican is designed for files => pages.
# Use variables (below) to set pieces of pages.

# sunflower yellow
INTROCOLOR  = "#fff"
ACOLOR      = "#edac00"
AHOVERCOLOR = "#b48400"
BRIGHTCOLOR = "#f1ca1d"
TEMPLATE_PAGES = {
    'custom.css' : 'custom.css'
}

INTROBKG='img/main.jpg'
LINKSBKG='img/face.jpg'

# img/ should be in content/
# available at <url>/img
STATIC_PATHS = ['img']

# ---

# description appears between <p> tags, so don't include them

SITE_TITLE = "ginsberg bot flock"
SITE_DESCRIPTION = "Tweeting Allen Ginsberg poems forever"
GITEA_URL = "https://github.com/charlesreid1-bots/ginsberg-bot-flock"

# ---

about_md = markdown.Markdown(extensions=['extra','codehilite'],
                             output_format='html4')

ABOUT_SHORT = "About"

ABOUT_TITLE = "about the ginsberg bot flock"

ABOUT_TEXT = """

<br />

**What is the ginsberg bot flock?**

The ginsberg bot flock is a flock of twitter bots that each tweet 
the entire contents of different Allen Ginsberg poems,
tweeting the poem one line at a time.

The flock is implemented in Python and uses the 
[rainbow mind machine](https://pages.charlesreid1.com/rainbow-mind-machine)
library.

For more information about bots and bot flocks, see [bots.charlesreid1.com](https://bots.charlesreid1.com).

Find the bots on twitter at the [ginsberg bot flock twitter list](https://twitter.com/i/lists/1267145777006034944)

[@gbf_america](https://twitter.com/gbf_america) &bull;
[@gbf_auntrose](https://twitter.com/gbf_auntrose) &bull;
[@gbf_chicago](https://twitter.com/gbf_chicago) &bull;
[@gbf_cosmo](https://twitter.com/gbf_cosmo) &bull;
[@gbf_dc](https://twitter.com/gbf_dc) &bull;
[@gbf_deathfame](https://twitter.com/gbf_deathfame) &bull;
[@gbf_deathfronts](https://twitter.com/gbf_deathfronts) &bull;
[@gbf_ecologue](https://twitter.com/gbf_ecologue) &bull;
[@gbf_elegy](https://twitter.com/gbf_elegy) &bull;
[@gbf_fiveam](https://twitter.com/gbf_fiveam) &bull;
[@gbf_greyhound](https://twitter.com/gbf_greyhound) &bull;
[@gbf_hospital](https://twitter.com/gbf_hospital) &bull;
[@gbf_howl](https://twitter.com/gbf_howl) &bull;
[@gbf_kaddish](https://twitter.com/gbf_kaddish) &bull;
[@gbf_lion](https://twitter.com/gbf_lion) &bull;
[@gbf_money](https://twitter.com/gbf_money) &bull;
[@gbf_organ](https://twitter.com/gbf_organ) &bull;
[@gbf_sunflower](https://twitter.com/gbf_sunflower) &bull;
[@gbf_supermarket](https://twitter.com/gbf_supermarket) 

<br />

**Why build the ginsberg bot flock?**

The ginsberg bot flock was built to help drown out some of the noise on Twitter,
and to provide a juxtaposition of Allen Ginsberg poetry with the latest goings-on
in the Twitter timeline.

<br />
<br />

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Everybody&#39;s serious - everybody but me.</p>&mdash; America (@gbf_america) <a href="https://twitter.com/gbf_america/status/990474706443689986?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I&#39;m not sorry.</p>&mdash; America (@gbf_america) <a href="https://twitter.com/gbf_america/status/990449518566039553?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">I can&#39;t stand my own mind.</p>&mdash; America (@gbf_america) <a href="https://twitter.com/gbf_america/status/990249291355574272?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Eyes more intelligent glanced up to death newspapers</p>&mdash; Elegy Che Guevara (@gbf_elegy) <a href="https://twitter.com/gbf_elegy/status/990382174250520577?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Board Directors of United Fruit</p>&mdash; Elegy Che Guevara (@gbf_elegy) <a href="https://twitter.com/gbf_elegy/status/990306631140364288?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Smog-Manufacturing Trustees of Chicago U</p>&mdash; Elegy Che Guevara (@gbf_elegy) <a href="https://twitter.com/gbf_elegy/status/990307890874404864?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Acheson&#39;s mustache, Truman&#39;s bony hat</p>&mdash; Elegy Che Guevara (@gbf_elegy) <a href="https://twitter.com/gbf_elegy/status/990311669019492352?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">To go mad and hide in jungle on mule and point rifle at OAS</p>&mdash; Elegy Che Guevara (@gbf_elegy) <a href="https://twitter.com/gbf_elegy/status/990312928699076608?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">Which way does your beard point tonight?</p>&mdash; A Supermarket in CA (@gbf_supermarket) <a href="https://twitter.com/gbf_supermarket/status/990402864366301186?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">--and you, García Lorca, what were you doing down by the watermelons?</p>&mdash; A Supermarket in CA (@gbf_supermarket) <a href="https://twitter.com/gbf_supermarket/status/990319772091863040?ref_src=twsrc%5Etfw">April 28, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">bed-bug death-oil. Who&#39;ll soak my brain with death-oil?</p>&mdash; Death On All Fronts (@gbf_deathfronts) <a href="https://twitter.com/gbf_deathfronts/status/990494320665944065?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">say Revolutionary expert Computers:</p>&mdash; Death On All Fronts (@gbf_deathfronts) <a href="https://twitter.com/gbf_deathfronts/status/990489283210371072?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">who jumped off the Brooklyn Bridge this actually happened and walked away unknown and forgotten into the ghostly daze of Chinatown soup alleyways and firetrucks, not even one free beer,</p>&mdash; Howl (@gbf_howl) <a href="https://twitter.com/gbf_howl/status/990494465096794114?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">who jumped in limousines with the Chinaman of Oklahoma on the impulse of winter midnight streetlight smalltown rain,</p>&mdash; Howl (@gbf_howl) <a href="https://twitter.com/gbf_howl/status/990456670777044993?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">and I sang Spanish loyalist songs</p>&mdash; Aunt Rose (@gbf_auntrose) <a href="https://twitter.com/gbf_auntrose/status/990403526638497792?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">in a high squeaky voice</p>&mdash; Aunt Rose (@gbf_auntrose) <a href="https://twitter.com/gbf_auntrose/status/990404786267697152?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

<blockquote class="twitter-tweet" data-lang="en"><p lang="en" dir="ltr">(hysterical) the committee listening</p>&mdash; Aunt Rose (@gbf_auntrose) <a href="https://twitter.com/gbf_auntrose/status/990406045930434560?ref_src=twsrc%5Etfw">April 29, 2018</a></blockquote>

"""

ABOUT_DESCRIPTION = about_md.convert(ABOUT_TEXT)



# -----------


def make_pages():
    descr = ""

    # 
    # 
    # On The Web
    # 
    # 

    descr += "<h3 style='color: black;'>Ginsberg Bot Flock On The Web</h3>"

    # items format:     [ button text,    href url,    fa-icon ]
    items  = [
                [
                    "github.com/charlesreid1-bots/ginsberg-bot-flock",
                    "https://github.com/charlesreid1-bots/ginsberg-bot-flock",
                    "github"
                ],
                [
                    "pages.charlesreid1.com/b-ginsberg",
                    "https://pages.charlesreid1.com/b-ginsberg",
                    "globe"
                ],
            ]

    for item in items:
        button_text = item[0]
        button_link = item[1]
        button_icon = item[2]

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"

    # 
    # 
    # On The Twitter
    # 
    # 

    descr += "<h3 style='color: black;'>Ginsberg Bot Flock On Twitter</h3>"

    poems = ["america",
             "auntrose",
             "chicago",
             "cosmo",
             "dc",
             "deathfame",
             "deathfronts",
             "ecologue",
             "elegy",
             "fiveam",
             "greyhound",
             "hospital",
             "howl",
             "kaddish",
             "lion",
             "money",
             "organ",
             "sunflower",
             "supermarket"]

    for poem in poems:
        handle = "gbf_%s"%(poem)
        button_text = "@%s"%(handle)
        button_link = "https://twitter.com/%s"%(handle)
        button_icon = "twitter"

        descr += "<p><a class=\"btn btn-default btn-lg\" href=\"%s\">"%(button_link)
        descr += "<i class=\"fa fa-fw fa-2x fa-%s\"></i> %s"%(button_icon, button_text)
        descr += "</a></p>\n"

    descr += "\n"

    return descr



LINKS_TITLE = ""

LINKS_DESCRIPTION = make_pages()



# ---


CONTACT_TITLE = "Contact charlesreid1"

CONTACT_DESCRIPTION = """<p>@charlesreid1 is a full-time data engineer and part-time bot-wrangler working on
the intersection of cloud computing and genomics at UC Santa Cruz.</p>
<p>Get in touch:</p>
<p><a href="mailto:twitter@charlesreid1.com">twitter (at) charlesreid1.com</a></p>
"""

ATTRIBUTION = """
<p style="font-size: 12px;">Header image credit: <a href="https://commons.wikimedia.org/wiki/File:Allen_ginsberg_675.jpg">Wikimedia Commons</a>, photo released under the <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.en">CC BY-SA 3.0</a>

<p style="font-size: 12px;">Links image credit: <a href="https://www.flickr.com/photos/ig_gallery/albums/72157627207393728">John Hopkins</a>, photo &copy; 2018 <a href="https://hoppyx.com/about-hoppy/">Estate of John Hopkins</a>
"""


# --------------8<---------------------

DISPLAY_PAGES_ON_MENU = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
DEFAULT_PAGINATION = False
