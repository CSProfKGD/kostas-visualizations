"use client";

import { useEffect, useState } from "react";

type Theme = "light" | "dark";

type Visualization = {
  slug: string;
  title: string;
  description: string;
  category: string;
  href: string;
  linkLabel?: string;
  featured?: boolean;
};

const visualizations: Visualization[] = [
  {
    slug: "sphere-to-cubemap",
    title: "Sphere to Cubemap",
    description: "Six views. One environment.",
    category: "Projective Geometry",
    href: "https://github.com/CSProfKGD/sphere-to-cubemap",
    featured: true,
  },
  {
    slug: "sphere-to-erp",
    title: "Sphere to Equirectangular Projection",
    description: "Same world. Different coordinates.",
    category: "Projective Geometry",
    href: "https://github.com/CSProfKGD/sphere-to-equirectangular-projection",
  },
  {
    slug: "local-minimum",
    title: "Stuck in a Bad Local Minimum?",
    description: "Why descent can settle for less.",
    category: "Optimization",
    href: "https://drive.google.com/file/d/152g4rEaCUWYxlKoeqIGiFclYNPV5a1ol/view?usp=share_link",
    linkLabel: "Watch video",
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
    title: "Convolution Visualization",
    description: "Slide. Pointwise multiply. Sum. Repeat.",
    category: "Signal Processing",
    href: "https://drive.google.com/file/d/1170Cbv73a7XmUNXWXli-rCGe7KW_KXXF/view?usp=share_link",
    linkLabel: "Watch video",
  },
  {
    slug: "epipolar-geometry",
    title: "Epipolar Geometry",
    description: "The geometry behind stereo vision.",
    category: "Projective Geometry",
    href: "https://csprofkgd.github.io/epipolar-geometry-visualization/",
  },
];

function ArrowIcon() {
  return <span aria-hidden="true">↗</span>;
}

export default function Home() {
  const [theme, setTheme] = useState<Theme>("light");

  useEffect(() => {
    const saved = window.localStorage.getItem("visualizations-theme");
    const nextTheme: Theme = saved === "dark" || saved === "light"
      ? saved
      : window.matchMedia("(prefers-color-scheme: dark)").matches
        ? "dark"
        : "light";
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
          <a href="https://csprofkgd.github.io" target="_blank" rel="noreferrer">
            CSProfKGD <ArrowIcon />
          </a>
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
          <span>Projective Geometry · Optimization · Linear Algebra · Signal Processing · Calculus</span>
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
          <article className={`visualization-card${item.featured ? " featured" : ""}`} key={item.slug}>
            <a className="image-link" href={item.href} target="_blank" rel="noreferrer" aria-label={`Open ${item.title}`}>
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
              <span className="open-badge" aria-hidden="true"><ArrowIcon /></span>
            </a>
            <div className="card-copy">
              <div>
                <p className="category">{item.category}</p>
                <h3>{item.title}</h3>
                <p className="description">{item.description}</p>
              </div>
              <a className="card-link" href={item.href} target="_blank" rel="noreferrer">
                {item.linkLabel ?? "Open visualization"} <ArrowIcon />
              </a>
            </div>
          </article>
        ))}
      </section>

      <footer>
        <p className="copyright">© {new Date().getFullYear()} Konstantinos (Kosta) Derpanis</p>
      </footer>
    </main>
  );
}
