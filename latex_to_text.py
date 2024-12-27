import re
latex_to_text = {
    # Fractions and decorations
    r'\frac': 'fraction',
    r'\sqrt': 'square root',
    r'\overline': 'overline',
    r'\underline': 'underline',
    r'\widehat': 'wide hat',
    r'\widetilde': 'wide tilde',
    r'\overbrace': 'overbrace',
    r'\underbrace': 'underbrace',
    r'\overrightarrow': 'over right arrow',
    r'\overleftarrow': 'over left arrow',

    # Delimiters
    r'\lvert': 'left vertical bar',
    r'\rvert': 'right vertical bar',
    r'\vert': 'vertical bar',
    r'\Vert': 'double vertical bar',
    r'\langle': 'left angle bracket',
    r'\rangle': 'right angle bracket',
    r'\lceil': 'left ceiling',
    r'\rceil': 'right ceiling',
    r'\lfloor': 'left floor',
    r'\rfloor': 'right floor',
    r'\backslash': 'backslash',

    # Variable-sized symbols
    r'\sum': 'summation',
    r'lim':"limits",
    r'\lim':"limits",

    r'\prod': 'product',
    r'\coprod': 'coproduct',
    r'\int': 'integral',
    r'\oint': 'contour integral',
    r'\iint': 'double integral',
    r'\iiint': 'triple integral',
    r'\iiiint': 'quadruple integral',
    r'\bigcup': 'big union',
    r'\bigcap': 'big intersection',
    r'\bigoplus': 'big direct sum',
    r'\bigotimes': 'big tensor product',
    r'\bigvee': 'big logical or',
    r'\bigwedge': 'big logical and',
    r'\biguplus': 'big union of multisets',
    r'\bigodot': 'big dot',

    # Miscellaneous symbols
    r'\infty': 'infinity',
    r'\nabla': 'nabla',
    r'\partial': 'partial derivative',
    r'\eth': 'eth',
    r'\clubsuit': 'club suit',
    r'\diamondsuit': 'diamond suit',
    r'\heartsuit': 'heart suit',
    r'\spadesuit': 'spade suit',
    r'\cdots': 'centered dots',
    r'\vdots': 'vertical dots',
    r'\ldots': 'leading dots',
    r'\ddots': 'diagonal dots',
    r'\forall': 'for all',
    r'\exists': 'there exists',
    r'\nexists': 'does not exist',
    r'\emptyset': 'empty set',
    r'\varnothing': 'var nothing',
    r'\imath': 'dotless i',
    r'\jmath': 'dotless j',
    r'\ell': 'ell',
    r'\angle': 'angle',
    r'\measuredangle': 'measured angle',
    r'\sphericalangle': 'spherical angle',
    r'\triangle': 'triangle',
    r'\vartriangle': 'var triangle',
    r'\blacktriangle': 'black triangle',
    r'\blacksquare': 'black square',
    r'\circledS': 'circled S',

    # Mathematical constants and functions
    r'\Re': 'real part',
    r'\Im': 'imaginary part',
    r'\wp': 'Weierstrass p',
    r'\Bbbk': 'blackboard bold k',
    r'\sharp': 'sharp',
    r'\flat': 'flat',
    r'\natural': 'natural',
    r'\prime': 'prime',
    r'\backprime': 'back prime',
    r'\surd': 'square root',

    # Arrows
    r'\uparrow': 'up arrow',
    r'\Uparrow': 'double up arrow',
    r'\downarrow': 'down arrow',
    r'\Downarrow': 'double down arrow',
    r'\rightarrow': 'right arrow',
    r'\leftarrow': 'left arrow',
    r'\leftrightarrow': 'left-right arrow',

    # Greek letters (common ones included for context)
    r'\alpha': 'alpha',
    r'\beta': 'beta',
    r'\gamma': 'gamma',
    r'\delta': 'delta',
    r'\epsilon': 'epsilon',
    r'\zeta': 'zeta',
    r'\eta': 'eta',
    r'\theta': 'theta',
    r'\iota': 'iota',
    r'\kappa': 'kappa',
    r'\lambda': 'lambda',
    r'\mu': 'mu',
    r'\nu': 'nu',
    r'\xi': 'xi',
    r'\pi': 'pi',
    r'\rho': 'rho',
    r'\sigma': 'sigma',
    r'\tau': 'tau',
    r'\upsilon': 'upsilon',
    r'\phi': 'phi',
    r'\chi': 'chi',
    r'\psi': 'psi',
    r'\omega': 'omega'
}

# latex_code = r"\int_{1}^{10} x^2 \, dx + \int_{0}^{5} y^3 \, dy"
# latex_code=r"\frac{x+y}{b} + \frac{x+y}{z-w}"
# latex_code= r"""\left\{\begin{array}{l l}
# S = \displaystyle\int_{x} \left\{\displaystyle{\frac{1}{2}} \sum_{a} \partial^{\mu} \chi_{a} \partial_{\mu} \chi_{a} + V(\rho)\right\}
# \end{array}\right
# """
latex_code=r"\mathbf{2}+{\frac{1}{4}}+{\frac{3}{5}}"
copy=latex_code

#DETECTING SUBSCRIPTS AND SUBERSPRCIPTS
subscripts='_\{[^}]+\}|_[^\s^_{]'
superscripts = r'\^\{[^}]+\}|\^[^\s^_{}]'
present_subs=re.findall(subscripts,latex_code)
for sub in present_subs:
    if sub.startswith("_{"):
        copy=copy.replace(sub,f" subscript {sub[2:-1]} ")
    else:
        copy=copy.replace(sub,f" subscript {sub[1:]} ")

present_super=re.findall(superscripts,latex_code)
print('present super',present_super)
for super in present_super:
    if super.startswith("^{"):
        copy=copy.replace(super,f" superscript {super[2:-1]} ")
    else:
        copy=copy.replace(super,f" superscript {super[1:]} ")

# DETECT FRACTIONS
fractions_pattern = r"\\frac\{(?:[^{}]+|\\frac\{[^{}]+\}\{[^{}]+\})+\}\{(?:[^{}]+|\\frac\{[^{}]+\}\{[^{}]+\})+\}"

fractions = re.findall(fractions_pattern, latex_code)

for fraction in fractions:
    audible_text=''
    components_pattern = r"\\frac\{([^{}]+)\}\{([^{}]+)\}"
    match = re.search(components_pattern, fraction)
    audible_text+=' fraction '

    if match:
        numerator = match.group(1) 
        audible_text+=numerator +' over '
        denominator = match.group(2)
        audible_text+=denominator
        
    copy=copy.replace(fraction,audible_text)

#replace all latex with corresponding audible text value
for key, value in latex_to_text.items():
    copy = re.sub(re.escape(key), value, copy)

#then remove the special characters that may be left 

latex_ignore_commands = {
    r"\left": "",
    r"\right": "",
    r"\[": "",
    r"\]": "",
    r"\(": "",
    r"\)": "",
    r"\begin{equation}": "",
    r"\end{equation}": "",
    r"\begin{align}": "",
    r"\end{align}": "",
    r"\begin{array}": "",
    r"\end{array}": "",
    r"\begin{itemize}": "",
    r"\end{itemize}": "",
    r"\begin{enumerate}": "",
    r"\end{enumerate}": "",
    r"\begin{description}": "",
    r"\end{description}": "",
    r"\begin{proof}": "",
    r"\end{proof}": "",
    r"\begin{theorem}": "",
    r"\end{theorem}": "",
    r"\begin{lemma}": "",
    r"\end{lemma}": "",
    r"\begin{align*}": "",
    r"\end{align*}": "",
    r"\textbf{}": "",
    r"\textit{}": "",
    r"\underline{}": "",
    r"\emph{}": "",
    r"\mathcal{}": "",
    r"\mathbb{}": "",
    r"\mathbf{}": "",
    r"\mathsf{}": "",
    r"\mathit{}": "",
    r"\mathnormal{}": "",
    r"\mathscr{}": "",
    r"\mathfrak{}": "",
    r"\hspace{}": "",
    r"\vspace{}": "",
    r"\quad": "",
    r"\qquad": "",
    r"\leftskip": "",
    r"\rightskip": "",
    r"\indent": "",
    r"\hat{}": "",
    r"\tilde{}": "",
    r"\bar{}": "",
    r"\acute{}": "",
    r"\grave{}": "",
    r"\dot{}": "",
    r"\check{}": "",
    r"\breve{}": "",
    r"\big{}": "",
    r"\Big{}": "",
    r"\bigg{}": "",
    r"\Bigg{}": "",
    r"\cdots": "",
    r"\vdots": "",
    r"\ddots": "",
    r"\boxed{}": "",
    r"\cancel{}": "",
    r"\overline{}": "",
    r"\underline{}": "",
    r"\text{}": "",
    r"\displaystyle": "",
    r"\mathbf":"",
        "\\":"",
    ",":""
}
for key, value in latex_ignore_commands.items():
    copy = re.sub(re.escape(key), value, copy)


print(copy)    
