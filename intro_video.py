from manim import *

# Constants
FRAME_RATE = 30
DURATION_BRANDING = 10
DURATION_INTRO = 20

# Color Palette
DARK_BLUE = "#003366"
LIGHT_BLUE = "#66CCFF"
WHITE = "#FFFFFF"
LIGHT_GRAY = "#F0F0F0"
DARK_GRAY = "#333333"
GRADIENT_COLORS = [LIGHT_BLUE, DARK_BLUE]

# ------------------------------
# Utility Functions
# ------------------------------
def animated_text(text, color=WHITE, scale=1.0):
    t = Text(text, color=color).scale(scale)
    t.set_stroke(width=0.5, color=BLACK)
    return t

def add_particles(scene, n=15, radius=0.05, color=LIGHT_BLUE):
    """Adds small floating circles for subtle particle effects."""
    particles = VGroup()
    for _ in range(n):
        x = (scene.camera.frame_width / 2) * (2 * np.random.rand() - 1)
        y = (scene.camera.frame_height / 2) * (2 * np.random.rand() - 1)
        c = Circle(radius=radius, color=color, fill_opacity=0.4)
        c.move_to([x, y, 0])
        particles.add(c)
    scene.add(particles)
    scene.play(*[FadeIn(c, scale=0.5, run_time=1) for c in particles], run_time=2)
    return particles

# ------------------------------
# Scene Classes
# ------------------------------
class OpeningBranding(Scene):
    def construct(self):
        self.camera.background_color = LIGHT_GRAY

        # Background gradient shape
        bg_rect = Rectangle(width=14, height=8, fill_color=LIGHT_BLUE, fill_opacity=0.1, stroke_opacity=0)
        self.add(bg_rect)

        # Logo
        logo = ImageMobject("assets/images/imranslab_logo.png").scale(0.5)
        logo.generate_target()
        logo.target.scale(1.0).shift(UP*0.5).rotate(0.1)

        # Slogan with gradient
        slogan = animated_text("Inspiring minds, building futures", scale=0.9)
        slogan.set_color_by_gradient(*GRADIENT_COLORS)
        slogan.next_to(logo, DOWN)

        # Particle effects
        particles = add_particles(self, n=20)

        # Animate logo and slogan
        self.play(MoveToTarget(logo, run_time=2), FadeIn(logo))
        self.play(FadeIn(slogan, shift=UP), run_time=2)
        self.wait(DURATION_BRANDING)
        self.play(FadeOut(logo), FadeOut(slogan), FadeOut(particles), FadeOut(bg_rect))

class PersonalIntroduction(Scene):
    def construct(self):
        self.camera.background_color = WHITE

        # Background animated shapes
        bg_circles = VGroup()
        for i in range(3):
            circle = Circle(radius=2.5 + i, color=LIGHT_BLUE, fill_opacity=0.05).shift(DOWN*0.5)
            bg_circles.add(circle)
            self.add(circle)

        # Animated texts
        intro_text = animated_text("Hello! I'm Naved Abrar Nibir", color=DARK_BLUE, scale=1.3)
        fun_fact = animated_text("Fun fact: I love building web projects and exploring AI", color=DARK_GRAY, scale=0.8)
        excitement = animated_text("Excited to join Imran's Lab!", color=LIGHT_BLUE, scale=1.1)

        fun_fact.next_to(intro_text, DOWN)
        excitement.next_to(fun_fact, DOWN)

        # Entrance animations
        self.play(FadeIn(intro_text, shift=UP*0.5, run_time=1.5))
        self.play(FadeIn(fun_fact, shift=RIGHT*0.5, run_time=1.5))
        self.play(FadeIn(excitement, shift=LEFT*0.5, run_time=1.5))

        # Subtle rotation for background circles
        self.play(Rotate(bg_circles, angle=PI/12, run_time=DURATION_INTRO, rate_func=linear))

        # Exit animations
        self.wait(DURATION_INTRO)
        self.play(
            intro_text.animate.scale(0.8).shift(UP*2),
            fun_fact.animate.shift(DOWN*2),
            excitement.animate.shift(UP*2),
            FadeOut(bg_circles)
        )
        self.play(FadeOut(intro_text), FadeOut(fun_fact), FadeOut(excitement))

class ClosingBranding(Scene):
    def construct(self):
        self.camera.background_color = LIGHT_GRAY

        # Background gradient shape
        bg_rect = Rectangle(width=14, height=8, fill_color=LIGHT_BLUE, fill_opacity=0.05, stroke_opacity=0)
        self.add(bg_rect)

        # Thank you text
        thank_you = animated_text("Thank you for watching!", color=DARK_BLUE, scale=1.5)
        thank_you.set_color_by_gradient(LIGHT_BLUE, DARK_BLUE)
        slogan = animated_text("Stay curious and keep learning", color=DARK_GRAY, scale=1.0)
        slogan.next_to(thank_you, DOWN)

        # Background floating circles
        particles = add_particles(self, n=15, radius=0.05, color=LIGHT_BLUE)

        # Entrance animations
        self.play(FadeIn(thank_you, shift=UP*0.5, run_time=2))
        self.play(Write(slogan, run_time=2))

        # Subtle rotation animation for background shapes
        self.play(Rotate(particles, angle=PI/6, run_time=4))

        # Exit animations
        self.wait(DURATION_BRANDING)
        self.play(FadeOut(thank_you), FadeOut(slogan), FadeOut(bg_rect), FadeOut(particles))
