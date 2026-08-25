"use client";

import { useEffect, useState } from "react";

type Theme = "light" | "dark";

type Visualization = {
  slug: string;
  title: string;
  description: string;
  category: string;
  href: string;
  featured?: boolean;
};

const visualizations: Visualization[] = [
  {
    slug: "sphere-to-cubemap",
    title: "Sphere to Cubemap",
    description: "Six views. One environment.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/sphere-to-cubemap/",
    featured: true,
  },
  {
    slug: "sphere-to-erp",
    title: "Sphere to Equirectangular Projection",
    description: "Same world. Different coordinates.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/sphere-to-equirectangular-projection/",
  },
  {
    slug: "local-minimum",
    title: "Stuck in a Bad Local Minimum?",
    description: "Why descent can settle for less.",
    category: "Optimization",
    href: "https://drive.google.com/file/d/152g4rEaCUWYxlKoeqIGiFclYNPV5a1ol/view?usp=share_link",
  },
  {
    slug: "gradient-descent",
    title: "Gradient Descent",
    description: "Tighten up your learning rate. We’re going down.",
    category: "Optimization",
    href: "https://csprofkgd.github.io/gradient-descent-lab/",
  },
  {
    slug: "partial-derivatives",
    title: "Partial Derivatives",
    description: "Hold one variable constant. Follow the curve. Read the slope.",
    category: "Calculus",
    href: "https://csprofkgd.github.io/partial-derivatives-visualization/",
  },
  {
    slug: "system-of-equations",
    title: "Interactive 3D System of Equations",
    description: "Where constraints meet, solutions appear.",
    category: "Linear Algebra",
    href: "https://csprofkgd.github.io/system-of-equations-visualization/",
  },
  {
    slug: "stereo-rectification",
    title: "Stereo Rectification",
    description: "From arbitrary cameras to parallel views.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/stereo-rectification-lab/",
    featured: true,
  },
  {
    slug: "parallel-stereo",
    title: "Parallel Stereo",
    description: "Two views. One point. One matching scanline.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/parallel-stereo-visualization/",
  },
  {
    slug: "planar-homography",
    title: "Planar Homography",
    description: "Plane-to-plane projective mapping.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/planar-homography-lab/",
  },
  {
    slug: "perspective-projection",
    title: "Perspective Projection",
    description: "One point. One ray. One image.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/perspective-projection/",
  },
  {
    slug: "convolution",
    title: "Correlation (aka \"Convolution\")",
    description: "Slide. Pointwise multiply. Sum. Repeat.",
    category: "Signal Processing",
    href: "https://drive.google.com/file/d/1170Cbv73a7XmUNXWXli-rCGe7KW_KXXF/view?usp=share_link",
  },
  {
    slug: "epipolar-geometry",
    title: "Epipolar Geometry",
    description: "The geometry behind stereo vision.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/epipolar-geometry-visualization/",
  },
];

export default function Home() {
  const [theme, setTheme] = useState<Theme>("dark");

  useEffect(() => {
    const saved = window.localStorage.getItem("visualizations-theme");
    const nextTheme: Theme = saved === "dark" || saved === "light" ? saved : "dark";
    setTheme(nextTheme);
    document.documentElement.dataset.theme = nextTheme;
  }, []);

  const changeTheme = () => {
    const nextTheme = theme === "dark" ? "light" : "dark";
    setTheme(nextTheme);
    document.documentElement.dataset.theme = nextTheme;
    window.localStorage.setItem("visualizations-theme", nextTheme);
  };

  return (
    <main className="gallery" data-theme={theme}>
      <nav className="nav-shell" aria-label="Primary navigation">
        <div className="nav-actions">
          <button
            className="theme-toggle"
            type="button"
            onClick={changeTheme}
            aria-label={`Switch to ${theme === "dark" ? "light" : "dark"} mode`}
          >
            <span className="theme-icon" aria-hidden="true">{theme === "dark" ? "☀" : "◐"}</span>
            {theme === "dark" ? "Light" : "Dark"}
          </button>
        </div>
      </nav>

      <header className="hero" id="top">
        <div className="hero-kicker">A visual learning collection by CSProfKGD</div>
        <h1>#KostasVisualizations</h1>
        <div className="hero-meta" aria-label="Collection summary">
          <span>12 interactive ideas</span>
          <span className="meta-divider" aria-hidden="true" />
          <span>Computer Vision · Machine Learning · Optimization</span>
        </div>
      </header>

      <section className="collection-intro" aria-labelledby="collection-title">
        <div>
          <p className="eyebrow">The collection</p>
          <h2 id="collection-title">See it. Move it. Understand it.</h2>
        </div>
        <p>
          Interactive visual explanations for the geometry and mathematics behind
          modern computer vision. Each experience turns an abstract construction
          into something you can inspect, manipulate, and understand.
        </p>
      </section>

      <section className="visualization-grid" aria-label="Visualization collection">
        {visualizations.map((item, index) => (
          <a
            className={`visualization-card${item.featured ? " featured" : ""}`}
            href={item.href}
            target="_blank"
            rel="noreferrer"
            aria-label={`Open ${item.title}`}
            data-slug={item.slug}
            key={item.slug}
          >
            <div className="image-link">
              <picture>
                <img
                  className="teaser-image teaser-light"
                  src={`/teasers/${item.slug}-light.png`}
                  alt={`${item.title} light-mode teaser`}
                  loading={index < 2 ? "eager" : "lazy"}
                />
                <img
                  className="teaser-image teaser-dark"
                  src={`/teasers/${item.slug}-dark.png`}
                  alt={`${item.title} dark-mode teaser`}
                  loading={index < 2 ? "eager" : "lazy"}
                />
              </picture>
            </div>
            <div className="card-copy">
              <div>
                <p className="category">{item.category}</p>
                <h3>{item.title}</h3>
                <p className="description">{item.description}</p>
              </div>
            </div>
          </a>
        ))}
      </section>

      <section className="instructor-section" aria-label="About Kosta Derpanis">
        <aside className="instructor-card">
          <img
            className="instructor-portrait"
            src="/KGD-profile.png"
            alt="Illustrated portrait of Kosta Derpanis"
          />
          <div className="instructor-copy">
            <p className="instructor-label">Your Tour Guide</p>
            <h2>Kosta Derpanis</h2>
            <p>Associate Professor<br />York University</p>
            <div className="instructor-links" aria-label="Kosta Derpanis links">
              <a href="https://csprofkgd.github.io" target="_blank" rel="noreferrer" aria-label="Homepage" title="Homepage">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M3 11.5 12 4l9 7.5" /><path d="M5.5 10.5V20h13v-9.5" /><path d="M9.5 20v-6h5v6" /></svg>
              </a>
              <a href="mailto:kosta@yorku.ca" aria-label="Email" title="Email">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6.5h16v11H4z" /><path d="m4.5 7 7.5 6 7.5-6" /></svg>
              </a>
              <a href="https://x.com/CSProfKGD" target="_blank" rel="noreferrer" aria-label="X" title="X">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13.9 10.5 21.3 2h-1.8l-6.4 7.4L8 2H2l7.8 11.3L2 22h1.8l6.8-7.8L16 22h6l-8.1-11.5Zm-2.4 2.7-.8-1.1L4.4 3.3h2.8l5 7 .8 1.1 6.6 9.3h-2.8l-5.3-7.5Z" /></svg>
              </a>
              <a href="https://www.linkedin.com/in/kosta-derpanis-a07824122/" target="_blank" rel="noreferrer" aria-label="LinkedIn" title="LinkedIn">
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.4 3H3.6c-.9 0-1.6.7-1.6 1.6v16.8c0 .9.7 1.6 1.6 1.6h16.8c.9 0 1.6-.7 1.6-1.6V4.6c0-.9-.7-1.6-1.6-1.6ZM8.1 19.7H5V9.9h3.1v9.8ZM6.6 8.5a1.8 1.8 0 1 1 0-3.6 1.8 1.8 0 0 1 0 3.6Zm13.1 11.2h-3.1v-4.8c0-1.1 0-2.6-1.6-2.6s-1.8 1.2-1.8 2.5v4.9h-3.1V9.9h3v1.3h.1c.4-.8 1.4-1.6 2.9-1.6 3.1 0 3.6 2 3.6 4.7v5.4Z" /></svg>
              </a>
            </div>
          </div>
        </aside>
      </section>

      <footer>
        <p className="copyright">© {new Date().getFullYear()} Konstantinos (Kosta) Derpanis</p>
      </footer>
    </main>
  );
}
