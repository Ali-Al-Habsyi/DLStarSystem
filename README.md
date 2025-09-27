\subsection*{Star-systematic configuration for illustration of direction for extension in Deep Learning}

Main file: Ytractorfunctional.py. Having access to all that surely knows currently, infer the rest as good as possible. Features, settings, assumed. $\text{Microscale} \rightarrow \text{Exascale}$. Datatypes: Numeric Array, Image, Sound (convertible to Image). Numeric Array $\rightarrow$ Image, by Image Generator, DeepDream. Build then extend, Learning links of links, Learning links, Notions Order of Links links between environments. The link is the dataset. Start rudimentarily with 5 nodes. Implement and report performance. Example: Inquiry towards $D5$. Access to $D1$ and $D2$. Try $D1 \rightarrow D5$ and $D2 \rightarrow D5$. Try $D1 \rightarrow D2 \rightarrow D5$ and $D2 \rightarrow D1 \rightarrow D5$$.

\begin{center}
\begin{tikzpicture}
\def\r{2}
\def\n{5}
\pgfmathsetmacro\m{\n-1}
\foreach \i in {0,...,\n}
\path ({90+\i*360/\n}:\r) coordinate (V\i);
\draw (V2)--(V0)--(V3)--(V1)--(V4)--cycle;
\def\Vlabel{{"$D_1$","$D_2$","$D_3$","$D_4$","$D_5$"}}
\foreach \i in {0,...,\m}{
\fill[red] (V\i) circle(2pt);
\path (0,0)--(V\i)--([turn]0:.4) 
node{\pgfmathparse{\Vlabel[\i]}\pgfmathresult}; 
}
\end{tikzpicture}
\end{center}

Inquiring into $D2$ requires some knowledge on $D2$ to be extended from data-environment. Call the above, Starlink Order 5. Starlink Order 1 works. Inquire into feature detection. The link is the dataset. The above graph is bidirectional in every edge. See https://github.com/Ali-Al-Habsyi/DLStarSystem for full implementation.

