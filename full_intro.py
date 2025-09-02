from manim import *

# ------------------ Paths ------------------ #
LOGO_PATH = r"assets/images/imranslab_logo.png"
NARRATION_PATH = r"assets/audio/narration_intro.mp3"

# ------------------ Full Intro Scene ------------------ #
class FullIntro(Scene):
    def construct(self):
        # ---------- Opening Branding ----------
        logo = ImageMobject(LOGO_PATH).scale(1.5)
        tagline = Text(
            "Innovating Education through Research",
            font_size=36
        ).next_to(logo, DOWN)

        # Play narration starting at 0s
        self.add_sound(NARRATION_PATH, time_offset=0)

        # Animations
        self.play(FadeIn(logo, shift=UP), run_time=2)
        self.play(Write(tagline), run_time=2)
        self.wait(3)
        self.play(FadeOut(logo), FadeOut(tagline))

        # ---------- Self Introduction ----------
        line1 = Text("Hi, I'm Naved Abrar Nibir.", font_size=48)
        line2 = Text(
            "Fun fact: I love combining creativity with coding.",
            font_size=36
        ).next_to(line1, DOWN, buff=0.6)
        line3 = Text(
            "I'm excited about this internship at Imranslab.",
            font_size=36
        ).next_to(line2, DOWN, buff=0.6)

        self.play(Write(line1), run_time=2)
        self.wait(2)  # wait for TTS pacing
        self.play(FadeIn(line2, shift=UP), run_time=2)
        self.wait(2)
        self.play(Write(line3), run_time=2)
        self.wait(3)
        self.play(FadeOut(line1), FadeOut(line2), FadeOut(line3))

        # ---------- Closing Branding ----------
        thank_you = Text(
            "Thank you for watching!",
            font_size=60,
            color=YELLOW
        )
        outro = Text(
            "Stay curious with Imranslab",
            font_size=40,
            color=BLUE
        ).next_to(thank_you, DOWN)

        self.play(FadeIn(thank_you, scale=0.5), run_time=2)
        self.play(Write(outro), run_time=2)
        self.wait(3)
        self.play(FadeOut(thank_you), FadeOut(outro))
