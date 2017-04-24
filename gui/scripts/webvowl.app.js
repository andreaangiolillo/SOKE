var d3 = require("d3");
var $ = require('jquery');

var file = $("#flag").val();



webvowl_1 = function(e) {
    function t(o) {
        if (n[o]) return n[o].exports;
        var r = n[o] = {
            exports: {},
            id: o,
            loaded: !1
        };
        return e[o].call(r.exports, r, r.exports, t), r.loaded = !0, r.exports
    }
    var n = {};
    return t.m = e, t.c = n, t.p = "", t(0)
}({
    0: function(e, t, n) {
        n(310), n(312), e.exports = n(313)
    },
    6: function(e, t) {
        e.exports = d3
    },
    86: function(e, t, n) {
        function o(e) {
            return null == e ? void 0 === e ? s : l : (e = Object(e), c && c in e ? i(e) : a(e))
        }
        var r = n(87),
            i = n(90),
            a = n(91),
            l = "[object Null]",
            s = "[object Undefined]",
            c = r ? r.toStringTag : void 0;
        e.exports = o
    },
    87: function(e, t, n) {
        var o = n(88),
            r = o.Symbol;
        e.exports = r
    },
    88: function(e, t, n) {
        var o = n(89),
            r = "object" == typeof self && self && self.Object === Object && self,
            i = o || r || Function("return this")();
        e.exports = i
    },
    89: function(e, t) {
        (function(t) {
            var n = "object" == typeof t && t && t.Object === Object && t;
            e.exports = n
        }).call(t, function() {
            return this
        }())
    },
    90: function(e, t, n) {
        function o(e) {
            var t = a.call(e, s),
                n = e[s];
            try {
                e[s] = void 0;
                var o = !0
            } catch (e) {}
            var r = l.call(e);
            return o && (t ? e[s] = n : delete e[s]), r
        }
        var r = n(87),
            i = Object.prototype,
            a = i.hasOwnProperty,
            l = i.toString,
            s = r ? r.toStringTag : void 0;
        e.exports = o
    },
    91: function(e, t) {
        function n(e) {
            return r.call(e)
        }
        var o = Object.prototype,
            r = o.toString;
        e.exports = n
    },
    98: function(e, t, n) {
        function o(e) {
            return "symbol" == typeof e || i(e) && r(e) == a
        }
        var r = n(86),
            i = n(99),
            a = "[object Symbol]";
        e.exports = o
    },
    99: function(e, t) {
        function n(e) {
            return null != e && "object" == typeof e
        }
        e.exports = n
    },
    107: function(e, t) {
        var n = Array.isArray;
        e.exports = n
    },
    149: function(e, t) {
        function n(e, t) {
            for (var n = -1, o = null == e ? 0 : e.length, r = Array(o); ++n < o;) r[n] = t(e[n], n, e);
            return r
        }
        e.exports = n
    },
    209: function(e, t, n) {
        function o(e) {
            return null == e ? "" : r(e)
        }
        var r = n(210);
        e.exports = o
    },
    210: function(e, t, n) {
        function o(e) {
            if ("string" == typeof e) return e;
            if (a(e)) return i(e, o) + "";
            if (l(e)) return d ? d.call(e) : "";
            var t = e + "";
            return "0" == t && 1 / e == -s ? "-0" : t
        }
        var r = n(87),
            i = n(149),
            a = n(107),
            l = n(98),
            s = 1 / 0,
            c = r ? r.prototype : void 0,
            d = c ? c.toString : void 0;
        e.exports = o
    },
    310: function(e, t) {},
    312: function(e, t) {
        function n() {
            var e, t, n = -1,
                o = /(?:\b(MS)?IE\s+|\bTrident\/7\.0;.*\s+rv:|\bEdge\/)(\d+)/.test(navigator.userAgent);
            if (o) return n = parseInt("12");
            var r = /Trident.*rv[ :]*11\./.test(navigator.userAgent);
            return r ? n = parseInt("11") : ("Microsoft Internet Explorer" === navigator.appName ? (e = navigator.userAgent, t = new RegExp("MSIE ([0-9]{1,}[\\.0-9]{0,})"), null !== t.exec(e) && (n = parseFloat(RegExp.$1))) : "Netscape" === navigator.appName && (e = navigator.userAgent, t = new RegExp("Trident/.*rv:([0-9]{1,}[\\.0-9]{0,})"), null !== t.exec(e) && (n = parseFloat(RegExp.$1))), n)
        }

        function o() {
            var e = n();
            if (e > 0 && e <= 12) {
                document.write('<div id="browserCheck">WebVOWL does not work properly in Internet Explorer and Microsoft Edge. Please use another browser, such as <a href="http://www.mozilla.org/firefox/">Mozilla Firefox</a> or <a href="https://www.google.com/chrome/">Google Chrome</a>, to run WebVOWL.</div>');
                var t = document.getElementById("canvasArea"),
                    o = document.getElementById("detailsArea"),
                    r = document.getElementById("optionsArea");
                t.className = "hidden", o.className = "hidden", r.className = "hidden"
            }
        }
        e.exports = o, o()
    },
    313: function(e, t, n) {
        (function(t) {
            e.exports = function() {
                function e(e, t, n) {
                    if (v.reset(), void 0 === e && void 0 === t) return void console.log("Nothing to load");
                    var o;
                    if (e) {
                        var r;
                        try {
                            o = JSON.parse(e), r = !0
                        } catch (e) {
                            r = !1
                        }
                        if (r === !1) return console.log("Retrieved data is not valid! (JSON.parse Error)"), void f.emptyGraphError();
                        if (!t) {
                            var s = o.header ? o.header.title : void 0,
                                d = l.textInLanguage(s);
                            t = d ? d : n
                        }
                    }
                    var u = parseInt(o.metrics.classCount),
                        p = parseInt(o.metrics.objectPropertyCount),
                        h = parseInt(o.metrics.datatypePropertyCount);
                    0 === u && 0 === p && 0 === h && f.emptyGraphError(), c.setJsonText(e), a.data(o), i.load(), m.updateOntologyInformation(o, L), c.setFilename(t)
                }

                function o() {
                    var e = t.select(s),
                        n = e.select("svg"),
                        o = window.innerHeight - 40,
                        r = window.innerWidth - .22 * window.innerWidth;
                    e.style("height", o + "px"), n.attr("width", r).attr("height", o), a.width(r).height(o), i.updateStyle(), y.updateVisibilityStatus()
                }
                var r = {},
                    i = webvowl.graph(),
                    a = i.graphOptions(),
                    l = webvowl.util.languageTools(),
                    s = "#graph",
                    c = n(314)(i),
                    d = n(315)(i),
                    u = n(316)(i),
                    p = n(317)(i),
                    f = n(318)(i),
                    v = n(322)(i),
                    h = n(323)(i),
                    g = n(324)(i),
                    y = n(325)(i),
                    m = n(326)(i),
                    b = webvowl.modules.colorExternalsSwitch(i),
                    x = webvowl.modules.compactNotationSwitch(i),
                    w = webvowl.modules.datatypeFilter(),
                    k = webvowl.modules.disjointFilter(),
                    C = webvowl.modules.focuser(),
                    S = webvowl.modules.emptyLiteralFilter(),
                    O = webvowl.modules.nodeDegreeFilter(d),
                    E = webvowl.modules.nodeScalingSwitch(i),
                    A = webvowl.modules.objectPropertyFilter(),
                    I = webvowl.modules.pickAndPin(),
                    D = webvowl.modules.selectionDetailsDisplayer(m.updateSelectionInformation),
                    L = webvowl.modules.statistics(),
                    M = webvowl.modules.subclassFilter(),
                    N = (document.getElementById("myProgress"), webvowl.modules.setOperatorFilter());
                return r.initialize = function() {
                    a.graphContainerSelector(s), a.selectionModules().push(C), a.selectionModules().push(D), a.selectionModules().push(I), a.filterModules().push(S), a.filterModules().push(L), a.filterModules().push(w), a.filterModules().push(A), a.filterModules().push(M), a.filterModules().push(k), a.filterModules().push(N), a.filterModules().push(E), a.filterModules().push(O), a.filterModules().push(x), a.filterModules().push(b), t.select(window).on("resize", o), c.setup(), u.setup(), d.setup(w, A, M, k, N, O), p.setup(I, E, x, b), v.setup(), m.setup(), f.setup(e), h.setup([u, d, p, C, D, v]), g.setup(), y.setup(), a.literalFilter(S), a.filterMenu(d), a.modeMenu(p), a.gravityMenu(u), a.pausedMenu(v), a.pickAndPinModule(I), a.resetMenu(h), a.searchMenu(g), a.ontologyMenu(f), a.navigationMenu(y), a.sidebar(m), i.start(), o()
                }, r
            }
        }).call(t, n(6))
    },
    314: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n() {
                    var n, i, a, l = t.select(e.options().graphContainerSelector()).select("svg");
                    r(), s(), n = l.attr("version", 1.1).attr("xmlns", "http://www.w3.org/2000/svg").node().parentNode.innerHTML, n = "<!-- Created with WebVOWL (version " + webvowl.version + "), http://vowl.visualdataweb.org -->\n" + n, i = o(n), a = "data:image/svg+xml;base64," + btoa(i), p.attr("href", a).attr("download", f + ".svg"), c(), d()
                }

                function o(e) {
                    var t, n, o, r = [],
                        i = e.length;
                    for (t = 0; t < i; t++) n = e.charAt(t), o = n.charCodeAt(0), o < 128 ? r.push(n) : r.push("&#" + o + ";");
                    return r.join("")
                }

                function r() {
                    i(".text", [{
                        name: "font-family",
                        value: "Helvetica, Arial, sans-serif"
                    }, {
                        name: "font-size",
                        value: "12px"
                    }]), i(".subtext", [{
                        name: "font-size",
                        value: "9px"
                    }]), i(".text.instance-count", [{
                        name: "fill",
                        value: "#666"
                    }]), i(".external + text .instance-count", [{
                        name: "fill",
                        value: "#aaa"
                    }]), i(".cardinality", [{
                        name: "font-size",
                        value: "10px"
                    }]), i(".text, .embedded", [{
                        name: "pointer-events",
                        value: "none"
                    }]), i(".class, .object, .disjoint, .objectproperty, .disjointwith, .equivalentproperty, .transitiveproperty, .functionalproperty, .inversefunctionalproperty, .symmetricproperty, .allvaluesfromproperty, .somevaluesfromproperty", [{
                        name: "fill",
                        value: "#acf"
                    }]), i(".label .datatype, .datatypeproperty", [{
                        name: "fill",
                        value: "#9c6"
                    }]), i(".rdf, .rdfproperty", [{
                        name: "fill",
                        value: "#c9c"
                    }]), i(".literal, .node .datatype", [{
                        name: "fill",
                        value: "#fc3"
                    }]), i(".deprecated, .deprecatedproperty", [{
                        name: "fill",
                        value: "#ccc"
                    }]), i(".external, .externalproperty", [{
                        name: "fill",
                        value: "#36c"
                    }]), i("path, .nofill", [{
                        name: "fill",
                        value: "none"
                    }]), i("marker path", [{
                        name: "fill",
                        value: "#000"
                    }]), i(".class, path, line, .fineline", [{
                        name: "stroke",
                        value: "#000"
                    }]), i(".white, .subclass, .subclassproperty, .external + text", [{
                        name: "fill",
                        value: "#fff"
                    }]), i(".class.hovered, .property.hovered, .cardinality.hovered, .cardinality.focused, circle.pin, .filled.hovered, .filled.focused", [{
                        name: "fill",
                        value: "#f00"
                    }, {
                        name: "cursor",
                        value: "pointer"
                    }]), i(".focused, path.hovered", [{
                        name: "stroke",
                        value: "#f00"
                    }]), i(".indirect-highlighting, .feature:hover", [{
                        name: "fill",
                        value: "#f90"
                    }]), i(".values-from", [{
                        name: "stroke",
                        value: "#69c"
                    }]), i(".symbol, .values-from.filled", [{
                        name: "fill",
                        value: "#69c"
                    }]), i(".class, path, line", [{
                        name: "stroke-width",
                        value: "2"
                    }]), i(".fineline", [{
                        name: "stroke-width",
                        value: "1"
                    }]), i(".dashed, .anonymous", [{
                        name: "stroke-dasharray",
                        value: "8"
                    }]), i(".dotted", [{
                        name: "stroke-dasharray",
                        value: "3"
                    }]), i("rect.focused, circle.focused", [{
                        name: "stroke-width",
                        value: "4px"
                    }]), i(".nostroke", [{
                        name: "stroke",
                        value: "none"
                    }]), i("marker path", [{
                        name: "stroke-dasharray",
                        value: "100"
                    }])
                }

                function i(e, n) {
                    var o = t.selectAll(e);
                    o.empty() || n.forEach(function(e) {
                        o.each(function() {
                            var n = t.select(this);
                            a(n, e.name) || n.style(e.name, e.value)
                        })
                    })
                }

                function a(e, t) {
                    return "fill" === t && l(e)
                }

                function l(e) {
                    var t = e.datum();
                    return t.backgroundColor && !!t.backgroundColor()
                }

                function s() {
                    t.selectAll(".hidden-in-export").style("display", "none")
                }

                function c() {
                    t.selectAll(".text, .subtext, .text.instance-count, .external + text .instance-count, .cardinality, .text, .embedded, .class, .object, .disjoint, .objectproperty, .disjointwith, .equivalentproperty, .transitiveproperty, .functionalproperty, .inversefunctionalproperty, .symmetricproperty, .allvaluesfromproperty, .somevaluesfromproperty, .label .datatype, .datatypeproperty, .rdf, .rdfproperty, .literal, .node .datatype, .deprecated, .deprecatedproperty, .external, .externalproperty, path, .nofill, .symbol, .values-from.filled, marker path, .class, path, line, .fineline, .white, .subclass, .subclassproperty, .external + text, .class.hovered, .property.hovered, .cardinality.hovered, .cardinality.focused, circle.pin, .filled.hovered, .filled.focused, .focused, path.hovered, .indirect-highlighting, .feature:hover, .values-from, .class, path, line, .fineline, .dashed, .anonymous, .dotted, rect.focused, circle.focused, .nostroke, marker path").each(function() {
                        var e = t.select(this),
                            n = e.node().style;
                        for (var o in n)
                            if (n.hasOwnProperty(o)) {
                                if (a(e, o)) continue;
                                e.style(o, null)
                            }
                        e.datum && e.datum().type && "rdfs:subClassOf" === e.datum().type() && e.style("fill", null)
                    })
                }

                function d() {
                    t.selectAll(".hidden-in-export").style("display", null)
                }

                function u() {
                    if (!h) return alert("No graph data available."), void t.event.preventDefault();
                    var n, o = e.graphNodeElements(),
                        r = e.graphLabelElements(),
                        i = JSON.parse(h),
                        a = i._comment,
                        l = " [Additional Information added by WebVOWL Exporter Version: 1.0.1]";
                    a.indexOf(l) === -1 && (i._comment = a + " [Additional Information added by WebVOWL Exporter Version: 1.0.1]");
                    var s = i.classAttribute,
                        c = i.propertyAttribute;
                    for (n = 0; n < s.length; n++) {
                        var d = s[n];
                        delete d.pos, delete d.pinned
                    }
                    var u;
                    for (n = 0; n < c.length; n++) u = c[n], delete u.pos, delete u.pinned;
                    o.each(function(e) {
                        var t = e.id();
                        for (n = 0; n < s.length; n++) {
                            var o = s[n];
                            if (o.id === t) {
                                o.pos = [e.x, e.y], e.pinned() && (o.pinned = !0);
                                break
                            }
                        }
                    });
                    for (var p = 0; p < r.length; p++) {
                        var g = r[p].property();
                        for (n = 0; n < c.length; n++)
                            if (u = c[n], u.id === g.id()) {
                                u.pos = [r[p].x, r[p].y], r[p].pinned() && (u.pinned = !0);
                                break
                            }
                    }
                    i.settings = {};
                    var y = e.scaleFactor(),
                        m = e.paused(),
                        b = e.translation();
                    i.settings.global = {}, i.settings.global.zoom = y, i.settings.global.translation = b, i.settings.global.paused = m;
                    var x, w, k, C = e.options().classDistance(),
                        S = e.options().datatypeDistance();
                    i.settings.gravity = {}, i.settings.gravity.classDistance = C, i.settings.gravity.datatypeDistance = S;
                    var O = e.options().filterMenu(),
                        E = O.getCheckBoxContainer(),
                        A = [];
                    for (n = 0; n < E.length; n++) x = E[n].checkbox.attr("id"), w = E[n].checkbox.property("checked"), k = {}, k.id = x, k.checked = w, A.push(k);
                    var I = O.getDegreeSliderValue();
                    i.settings.filter = {}, i.settings.filter.checkBox = A, i.settings.filter.degreeSliderValue = I;
                    var D = e.options().modeMenu(),
                        L = D.getCheckBoxContainer(),
                        M = [];
                    for (n = 0; n < L.length; n++) x = L[n].attr("id"), w = L[n].property("checked"), k = {}, k.id = x, k.checked = w, M.push(k);
                    var N = D.colorModeState();
                    i.settings.modes = {}, i.settings.modes.checkBox = M, i.settings.modes.colorSwitchState = N;
                    var j = {};
                    j._comment = i._comment, j.header = i.header, j.namespace = i.namespace, j.metrics = i.metrics, j.settings = i.settings, j.class = i.class, j.classAttribute = i.classAttribute, j.property = i.property, j.propertyAttribute = i.propertyAttribute;
                    var F = JSON.stringify(j, null, "  "),
                        R = "data:text/json;charset=utf-8," + encodeURIComponent(F);
                    v.attr("href", R).attr("download", f + ".json")
                }
                var p, f, v, h, g = {};
                return g.setup = function() {
                    p = t.select("#exportSvg").on("click", n), v = t.select("#exportJson").on("click", u);
                    var o = t.select("#export");
                    o.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    })
                }, g.setFilename = function(e) {
                    f = e || "export"
                }, g.setJsonText = function(e) {
                    h = e
                }, g
            }
        }).call(t, n(6))
    },
    315: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n(n, o, r, i) {
                    var a, l;
                    a = t.select(i).append("div").classed("checkboxContainer", !0), l = a.append("input").classed("filterCheckbox", !0).attr("id", o + "FilterCheckbox").attr("type", "checkbox").property("checked", n.enabled()), c.push({
                        checkbox: l,
                        defaultState: n.enabled()
                    }), l.on("click", function(t) {
                        var o = l.property("checked");
                        n.enabled(o), t !== !0 && e.update()
                    }), a.append("label").attr("for", o + "FilterCheckbox").text(r)
                }

                function o(t, n) {
                    t.setMaxDegreeSetter(function(e) {
                        l.attr("max", e), i(l, Math.min(e, l.property("value")))
                    }), t.setDegreeGetter(function() {
                        return +l.property("value")
                    }), t.setDegreeSetter(function(e) {
                        i(l, e)
                    });
                    var o, s;
                    o = n.append("div").classed("distanceSliderContainer", !0), l = o.append("input").attr("id", "nodeDegreeDistanceSlider").attr("type", "range").attr("min", 0).attr("step", 1), o.append("label").classed("description", !0).attr("for", "nodeDegreeDistanceSlider").text("Degree of collapsing"), s = o.append("label").classed("value", !0).attr("for", "nodeDegreeDistanceSlider").text(0), l.on("change", function(t) {
                        t !== !0 && (e.update(), a = l.property("value"))
                    }), l.on("input", function() {
                        var e = l.property("value");
                        s.text(e)
                    }), l.on("wheel", r), l.on("focusout", function() {
                        l.property("value") !== a && e.update()
                    })
                }

                function r() {
                    var n, o = t.event;
                    o.deltaY < 0 && (n = 1), o.deltaY > 0 && (n = -1);
                    var r = parseInt(l.property("value")),
                        i = r + n;
                    r !== i && (l.property("value", i), l.on("input")(), e.update())
                }

                function i(e, t) {
                    e.property("value", t).on("input")()
                }
                var a, l, s = {},
                    c = [],
                    d = t.select("#filterOption a"),
                    u = t.select("#nodeDegreeFilteringOption");
                return s.getCheckBoxContainer = function() {
                    return c
                }, s.getDegreeSliderValue = function() {
                    return l.property("value")
                }, s.setup = function(r, i, a, l, c, p) {
                    var f = t.select("#filterOption");
                    f.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    }), d.on("mouseleave", function() {
                        s.highlightForDegreeSlider(!1)
                    }), n(r, "datatype", "Datatype properties", "#datatypeFilteringOption"), n(i, "objectProperty", "Object properties", "#objectPropertyFilteringOption"), n(a, "subclass", "Solitary subclasses", "#subclassFilteringOption"), n(l, "disjoint", "Class disjointness", "#disjointFilteringOption"), n(c, "setoperator", "Set operators", "#setOperatorFilteringOption"), o(p, u)
                }, s.reset = function() {
                    c.forEach(function(e) {
                        var t = e.checkbox,
                            n = e.defaultState,
                            o = t.property("checked");
                        o !== n && (t.property("checked", n), t.on("click")())
                    }), i(l, 0), l.on("change")()
                }, s.highlightForDegreeSlider = function(e) {
                    if (arguments.length || (e = !0), d.classed("highlighted", e), u.classed("highlighted", e), d.classed("buttonPulse") === !0 && e === !0) {
                        d.classed("buttonPulse", !1);
                        var t = setTimeout(function() {
                            d.classed("buttonPulse", e), clearTimeout(t)
                        }, 100)
                    } else d.classed("buttonPulse", e)
                }, s.setCheckBoxValue = function(e, t) {
                    for (var n = 0; n < c.length; n++) {
                        var o = c[n].checkbox.attr("id");
                        if (o === e) {
                            c[n].checkbox.property("checked", t);
                            break
                        }
                    }
                }, s.setDegreeSliderValue = function(e) {
                    l.property("value", e)
                }, s.updateSettings = function() {
                    var e = !0,
                        t = l.property("value");
                    t > 0 ? s.highlightForDegreeSlider(!0) : s.highlightForDegreeSlider(!1), c.forEach(function(t) {
                        var n = t.checkbox;
                        n.on("click")(e)
                    }), l.on("input")(), l.on("change")(e)
                }, s
            }
        }).call(t, n(6))
    },
    316: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n(n, r, a, l) {
                    var s, c, d = l();
                    s = t.select(n).append("div").datum({
                        distanceFunction: l
                    }).classed("distanceSliderContainer", !0);
                    var u = s.append("input").attr("id", r + "DistanceSlider").attr("type", "range").attr("min", 10).attr("max", 600).attr("value", l()).attr("step", 10);
                    s.append("label").classed("description", !0).attr("for", r + "DistanceSlider").text(a), c = s.append("label").classed("value", !0).attr("for", r + "DistanceSlider").text(l()), i.push(u), u.on("focusout", function() {
                        e.updateStyle()
                    }), u.on("input", function() {
                        var t = u.property("value");
                        l(t), o(d), c.text(t), e.updateStyle()
                    }), u.on("wheel", function() {
                        var e, n = t.event;
                        n.deltaY < 0 && (e = 10), n.deltaY > 0 && (e = -10);
                        var o = parseInt(u.property("value")),
                            r = o + e;
                        r !== o && (u.property("value", r), l(r), u.on("input")())
                    })
                }

                function o(e) {
                    var t = Math.max(a.classDistance(), a.datatypeDistance()),
                        n = t / e,
                        o = l * n;
                    a.charge(o)
                }
                var r = {},
                    i = [],
                    a = e.graphOptions(),
                    l = a.charge();
                return r.setup = function() {
                    var o = t.select("#gravityOption");
                    o.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    }), n("#classSliderOption", "class", "Class distance", a.classDistance), n("#datatypeSliderOption", "datatype", "Datatype distance", a.datatypeDistance)
                }, r.reset = function() {
                    i.forEach(function(e) {
                        e.property("value", function(e) {
                            return e.distanceFunction()
                        }), e.on("input")()
                    })
                }, r
            }
        }).call(t, n(6))
    },
    317: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n(n, o, r, i, a) {
                    var l, s;
                    return l = t.select(i).append("div").classed("checkboxContainer", !0).datum({
                        module: n,
                        defaultState: n.enabled()
                    }), s = l.append("input").classed("moduleCheckbox", !0).attr("id", o + "ModuleCheckbox").attr("type", "checkbox").property("checked", n.enabled()), d.push(s), s.on("click", function(t, n) {
                        var o = s.property("checked");
                        t.module.enabled(o), a && n !== !0 && e.update()
                    }), l.append("label").attr("for", o + "ModuleCheckbox").text(r), l
                }

                function o(t, n) {
                    var o = t.append("button").datum({
                        active: !1
                    }).classed("color-mode-switch", !0);
                    return r(o, n), o.on("click", function(t) {
                        var i = o.datum();
                        i.active = !i.active, r(o, n), n.enabled() && t !== !0 && e.update()
                    }), o
                }

                function r(e, t) {
                    var n = e.datum().active,
                        o = i(n);
                    e.classed("active", n).text(o.text), t && t.colorModeType(o.type)
                }

                function i(e) {
                    return e ? s : l
                }
                var a, l = {
                        text: "Multicolor",
                        type: "same"
                    },
                    s = {
                        text: "Multicolor",
                        type: "gradient"
                    },
                    c = {},
                    d = [];
                return c.colorModeState = function(e) {
                    return arguments.length ? (a.datum().active = e, c) : a.datum().active
                }, c.getCheckBoxContainer = function() {
                    return d
                }, c.colorModeSwitch = function() {
                    return a
                }, c.setup = function(r, i, l, s) {
                    var c = t.select("#moduleOption");
                    c.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    }), n(r, "pickandpin", "Pick & pin", "#pickAndPinOption", !1), n(i, "nodescaling", "Node scaling", "#nodeScalingOption", !0), n(l, "compactnotation", "Compact notation", "#compactNotationOption", !0);
                    var d = n(s, "colorexternals", "Color externals", "#colorExternalsOption", !0);
                    a = o(d, s)
                }, c.reset = function() {
                    d.forEach(function(e) {
                        var t = e.datum().defaultState,
                            n = e.property("checked");
                        n !== t && (e.property("checked", t), e.on("click")(e.datum())), e.datum().module.reset()
                    }), a.datum().active = !0, a.on("click")()
                }, c.setCheckBoxValue = function(e, t) {
                    for (var n = 0; n < d.length; n++) {
                        var o = d[n].attr("id");
                        if (o === e) {
                            d[n].property("checked", t);
                            break
                        }
                    }
                }, c.setColorSwitchState = function(e) {
                    c.colorModeState(!e)
                }, c.updateSettings = function() {
                    var e = !0;
                    d.forEach(function(t) {
                        t.on("click")(t.datum(), e)
                    }), a.on("click")(e)
                }, c
            }
        }).call(t, n(6))
    },
    318: function(e, t, n) {
        (function(t) {
            var o = n(319);
            e.exports = function(e) {
                function n() {
                    i(), t.select(window).on("hashchange", function() {
                        var e = t.event.oldURL,
                            n = t.event.newURL;
                        if (e !== n) {
                            if (n === e + "#") return;
                            r(), i()
                        }
                    }), r()
                }

                function r() {
                    t.selectAll("#optionsMenu > li > a").attr("href", location.hash || "#")
                }

                function i() {
                    var e = location.hash.slice(1);
                    e || (e = k);
                    var n = t.selectAll(".select li").classed("selected-ontology", !1);
                    O = !1;
                    var o = "iri=",
                        r = "url=",
                        i = "file=";
                    if (e.substr(0, i.length) === i) {
                        var s = decodeURIComponent(e.slice(i.length));
                        d(s)
                    } else if (e.substr(0, r.length) === r) {
                        var c = decodeURIComponent(e.slice(r.length));
                        a("read?json=" + encodeURIComponent(c), c)
                    } else if (e.substr(0, o.length) === o) {
                        var u = decodeURIComponent(e.slice(o.length));
                        l("convert?iri=" + encodeURIComponent(u), u), t.select("#converter-option").classed("selected-ontology", !0)
                    } else l("data/json/" + e + ".json", e), n.each(function() {
                        var n = t.select(this);
                        n.select("a").size() > 0 && n.select("a").attr("href") === "#" + e && n.classed("selected-ontology", !0)
                    })
                }

                function a(n, o) {
                    b = o;
                    var r = E[n],
                        i = o.replace(/\/$/g, ""),
                        a = i.slice(i.lastIndexOf("/") + 1),
                        l = o.toLowerCase().endsWith(".json");
                    return l ? void(r ? (x(r, void 0, a), g(!0)) : (h(), t.xhr(n, "application/json", function(t, o) {
                        var r, i = !t;
                        if (null !== t && 500 === t.status || o && 0 === o.responseText.length) return y(), w.notValidJsonURL(), void(E[n] = void 0);
                        var l;
                        i ? (l = o.responseText, E[n] = l) : 404 === t.status && (r = "Connection to the OWL2VOWL interface could not be established.", e.clearGraphData()), x(l, void 0, a), g(i, t ? t.response : void 0, r), O === !0 && (w.notValidJsonFile(), e.clearGraphData()), y()
                    }))) : (w.notValidJsonURL(), void e.clearGraphData())
                }

                function l(n, o) {
                    b = o;
                    var r = E[n],
                        i = o.replace(/\/$/g, ""),
                        a = i.slice(i.lastIndexOf("/") + 1);
                    r ? (x(r, void 0, a), g(!0)) : (h(), t.xhr(n, "application/json", function(t, o) {
                        var r, i = !t;
                        if (null !== t && 500 === t.status) return y(), void w.emptyGraphError();
                        var l;
                        if (i) l = o.responseText, E[n] = l;
                        else if (404 === t.status) {
                            var s = "iri=",
                                c = "url=",
                                d = "file=",
                                u = location.hash.slice(1);
                            u.substr(0, d.length) !== d && u.substr(0, c.length) !== c && u.substr(0, s.length) !== s && w.emptyGraphError(), r = "Connection to the OWL2VOWL interface could not be established.", e.clearGraphData()
                        }
                        x(l, void 0, a), g(i, t ? t.response : void 0, r), O === !0 && (w.emptyGraphError(), e.clearGraphData()), y()
                    }))
                }

                function s() {
                    var e = t.select("#iri-converter-button"),
                        n = t.select("#iri-converter-input");
                    n.on("input", function() {
                        v();
                        var t = "" === n.property("value");
                        e.attr("disabled", t || void 0)
                    }).on("click", function() {
                        v()
                    }), t.select("#iri-converter-form").on("submit", function() {
                        for (var e = n.property("value"), o = e.replace(/%20/g, " "); o.beginsWith(" ");) o = o.substr(1, o.length);
                        for (; o.endsWith(" ");) o = o.substr(0, o.length - 1);
                        e = o;
                        var r = e.toLowerCase();
                        return r.endsWith(".json") ? (console.log("file is an URL for a json "), location.hash = "url=" + e, n.property("value", ""), n.on("input")()) : (location.hash = "iri=" + e, n.property("value", ""), n.on("input")()), t.event.preventDefault(), !1
                    })
                }

                function c() {
                    var e = t.select("#file-converter-input"),
                        n = t.select("#file-converter-label"),
                        o = t.select("#file-converter-button");
                    e.on("change", function() {
                        var t = e.property("files");
                        t.length <= 0 ? (n.text("Select ontology file"), o.property("disabled", !0)) : (n.text(t[0].name), o.property("disabled", !1), v())
                    }), o.on("click", function() {
                        var t = e.property("files")[0];
                        if (!t) return !1;
                        var n = "file=" + t.name;
                        location.hash === "#" + n ? d() : location.hash = n
                    })
                }

                function d(n) {
                    var o = E[n];
                    if (o) return h(), x(o, n), g(!0), O === !0 && w.emptyGraphError(), void y();
                    var r = t.select("#file-converter-input").property("files")[0];
                    return !r || n && n !== r.name ? (x(void 0, void 0), g(!1, void 0, 'No cached version of "' + n + '" was found. Please reupload the file.'), void e.clearGraphData()) : (n = r.name, void(n.match(/\.json$/) ? (h(), u(r, n)) : p(r, n, !0)))
                }

                function u(e, t) {
                    var n = new FileReader;
                    n.readAsText(e), n.onload = function() {
                        h(), f(n.result, t), g(!0), O === !0 && w.emptyGraphError(), y()
                    }
                }

                function p(n, o, r) {
                    var i = t.select("#file-converter-button");
                    h(), i.property("disabled", !0);
                    var a = new FormData;
                    a.append("ontology", n);
                    var l = new XMLHttpRequest;
                    l.open("POST", "convert", !0), l.onload = function() {
                        i.property("disabled", !1), 200 === l.status ? (f(l.responseText, o), E[o] = l.responseText) : (x(void 0, void 0), g(!1, l.responseText), y(), e.clearGraphData()), y(), O === !0 && r === !0 && (console.log("Failed to convert the file"), E[o] = void 0, w.notValidJsonFile())
                    }, l.send(a)
                }

                function f(e, t) {
                    var n = t.split(".")[0];
                    x(e, n)
                }

                function v() {
                    function e() {
                        n.style("display", void 0), clearTimeout(m), t.select(window).on("click", void 0).on("keydown", void 0), n.on("mouseover", void 0)
                    }
                    var n = t.select("#select .toolTipMenu");
                    n.on("click", function() {
                        t.event.stopPropagation()
                    }).on("keydown", function() {
                        t.event.stopPropagation()
                    }), n.style("display", "block"), clearTimeout(m), m = setTimeout(function() {
                        e()
                    }, 3e3), t.select(window).on("click", function() {
                        e()
                    }).on("keydown", function() {
                        e()
                    }), n.on("mouseover", function() {
                        e()
                    })
                }

                function h() {
                    C.classed("hidden", !0), S.classed("hidden", !1)
                }

                function g(e, n, r) {
                    C.classed("hidden", e);
                    var i = t.select("#error-info");
                    r ? i.text(r) : i.html('Ontology could not be loaded.<br>Is it a valid OWL ontology? Please check with <a target="_blank"href="http://visualdataweb.de/validator/">OWL Validator</a>.');
                    var a = !n,
                        l = t.select("#error-description-button").classed("hidden", a).datum().open;
                    t.select("#error-description-container").classed("hidden", a || !l), t.select("#error-description").text(o(n))
                }

                function y() {
                    S.classed("hidden", !0)
                }
                var m, b, x, w = {},
                    k = file,
                    C = t.select("#loading-error"),
                    S = t.select("#loading-progress"),
                    O = !1,
                    E = {};
                return String.prototype.beginsWith = function(e) {
                    return 0 === this.indexOf(e)
                }, w.setup = function(o) {
                    x = o;
                    var r = t.select("#select");
                    r.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    }), s(), c();
                    var i = t.select("#error-description-button").datum({
                        open: !1
                    });
                    i.on("click", function(e) {
                        var n = t.select("#error-description-container"),
                            o = t.select(this);
                        e.open = !e.open;
                        var r = e.open;
                        r ? o.text("Hide error details") : o.text("Show error details"), n.classed("hidden", !r)
                    }), n()
                }, w.setIriText = function(e) {
                    var n = t.select("#iri-converter-input");
                    n.node().value = e;
                    var o = t.select("#iri-converter-button");
                    o.attr("disabled", !1), t.select("#iri-converter-form").on("submit")()
                }, w.emptyGraphError = function() {
                    O = !0, C.classed("hidden", !1);
                    var n = t.select("#error-info");
                    n.text("There is nothing to visualize.");
                    var o = "There is no OWL input under the given IRI(" + b + "). Please try to load the OWL file directly.",
                        r = !o,
                        i = t.select("#error-description-button").classed("hidden", r).datum().open;
                    t.select("#error-description-container").classed("hidden", r || !i), t.select("#error-description").text(o), e.clearGraphData()
                }, w.notValidJsonURL = function() {
                    O = !0, C.classed("hidden", !1);
                    var n = t.select("#error-info");
                    n.text("Invalid JSON URL");
                    var o = "There is no JSON input under the given URL(" + b + "). Please try to load the JSON file directly.",
                        r = !o,
                        i = t.select("#error-description-button").classed("hidden", r).datum().open;
                    t.select("#error-description-container").classed("hidden", r || !i), t.select("#error-description").text(o), e.clearGraphData()
                }, w.notValidJsonFile = function() {
                    O = !0, C.classed("hidden", !1);
                    var n = t.select("#error-info");
                    n.text("Invalid JSON file");
                    var o = "The uploaded file is not a valid JSON file. (" + b + ")",
                        r = !o,
                        i = t.select("#error-description-button").classed("hidden", r).datum().open;
                    t.select("#error-description-container").classed("hidden", r || !i), t.select("#error-description").text(o), e.clearGraphData()
                }, w
            }
        }).call(t, n(6))
    },
    319: function(e, t, n) {
        function o(e) {
            return e = r(e), e && l.test(e) ? e.replace(a, i) : e
        }
        var r = n(209),
            i = n(320),
            a = /&(?:amp|lt|gt|quot|#39);/g,
            l = RegExp(a.source);
        e.exports = o
    },
    320: function(e, t, n) {
        var o = n(321),
            r = {
                "&amp;": "&",
                "&lt;": "<",
                "&gt;": ">",
                "&quot;": '"',
                "&#39;": "'"
            },
            i = o(r);
        e.exports = i
    },
    321: function(e, t) {
        function n(e) {
            return function(t) {
                return null == e ? void 0 : e[t]
            }
        }
        e.exports = n
    },
    322: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n() {
                    o(), r()
                }

                function o() {
                    i.classed("paused", function(e) {
                        return e.paused
                    })
                }

                function r() {
                    i.datum().paused ? i.text("Resume") : i.text("Pause")
                }
                var i, a = {};
                return a.setup = function() {
                    var o = t.select("#pauseOption");
                    o.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    }), i = t.select("#pause-button").datum({
                        paused: !1
                    }).on("click", function(t) {
                        e.paused(!t.paused), t.paused = !t.paused, n(), i.classed("highlighted", t.paused), e.options().navigationMenu().updateVisibilityStatus()
                    }), n()
                }, a.setPauseValue = function(t) {
                    i.datum().paused = t, e.paused(t), i.classed("highlighted", t), n()
                }, a.reset = function() {
                    a.setPauseValue(!1)
                }, a
            }
        }).call(t, n(6))
    },
    323: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n() {
                    i.classDistance(a.classDistance()), i.datatypeDistance(a.datatypeDistance()), i.charge(a.charge()), i.gravity(a.gravity()), i.linkStrength(a.linkStrength()), e.reset(), o.forEach(function(e) {
                        e.reset()
                    }), e.updateStyle()
                }
                var o, r = {},
                    i = e.graphOptions(),
                    a = webvowl.options();
                return r.setup = function(r) {
                    o = r, t.select("#reset-button").on("click", n);
                    var i = t.select("#resetOption");
                    i.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    })
                }, r
            }
        }).call(t, n(6))
    },
    324: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n() {
                    v = e.getUpdateDictionary(), x = !1, y = [], m = [];
                    var t, n = [],
                        o = [];
                    for (t = 0; t < v.length; t++) {
                        var r = v[t].labelForCurrentLanguage();
                        n.push(v[t].id()), o.push(r)
                    }
                    p = [], f = [];
                    var i, a, l = -1;
                    for (t = 0; t < o.length; t++)
                        if (0 !== t)
                            if (i = o[t], a = n[t], l = p.indexOf(i), l === -1) {
                                p.push(o[t]), f.push([]);
                                var s = f.length;
                                f[s - 1].push(a)
                            } else f[l].push(a);
                    else p.push(o[t]), f.push([]), f[0].push(n[t]);
                    for (t = 0; t < p.length; t++) {
                        for (var c = p[t], d = f[t], u = "[ ", h = 0; h < d.length; h++) u += d[h].toString(), u += ", ";
                        u = u.substring(0, u.length - 2), u += " ]", d.length > 1 ? y.push(c + " (" + d.length + ")") : y.push(c), m.push(c)
                    }
                }

                function o() {
                    g.showSearchEntries()
                }

                function r() {
                    w ? g.hideSearchEntries() : g.showSearchEntries()
                }

                function i(e) {
                    var t = /^(https?|ftp):\/\/([a-zA-Z0-9.-]+(:[a-zA-Z0-9.&%$-]+)*@)*((25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9][0-9]?)(\.(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])){3}|([a-zA-Z0-9-]+\.)*[a-zA-Z0-9-]+\.(com|edu|gov|int|mil|net|org|biz|arpa|info|name|pro|aero|coop|museum|[a-zA-Z]{2}))(:[0-9]+)*(\/($|[a-zA-Z0-9.,?'\\+&%$#=~_-]+))*$/;
                    return t.test(e)
                }

                function a() {
                    x && n();
                    var o, r = u.node().children,
                        a = r.length,
                        l = 0,
                        s = -1;
                    for (o = 0; o < a; o++) {
                        var c = r[o].getAttribute("class");
                        "dbEntrySelected" === c && (s = o)
                    }
                    if (13 === t.event.keyCode)
                        if (s >= 0 && s < a) r[s].onclick(), g.hideSearchEntries();
                        else if (0 === a) {
                        h = d.node().value;
                        for (var p = h.replace(/%20/g, " "); p.beginsWith(" ");) p = p.substr(1, p.length);
                        for (; p.endsWith(" ");) p = p.substr(0, p.length - 1);
                        var f = p.replace(/ /g, "%20"),
                            v = i(f);
                        if (v) {
                            var y = e.options().ontologyMenu();
                            y.setIriText(f), d.node().value = ""
                        } else console.log(f + " is not a valid URL!")
                    }
                    38 === t.event.keyCode && (l = -1, g.showSearchEntries()), 40 === t.event.keyCode && (l = 1, g.showSearchEntries());
                    var m = s + l;
                    m !== s && (m < 0 && s <= 0 && r[0].setAttribute("class", "dbEntrySelected"), m >= a && r[s].setAttribute("class", "dbEntrySelected"), m >= 0 && m < a && (r[m].setAttribute("class", "dbEntrySelected"), s >= 0 && r[s].setAttribute("class", "dbEntry")))
                }

                function l() {
                    var e, t;
                    h = d.node().value;
                    var n, o, r = [],
                        i = [],
                        a = h.toLowerCase();
                    for (n = 0; n < y.length; n++) {
                        var l = y[n];
                        void 0 !== l && (o = y[n].toLowerCase(), o.indexOf(a) > -1 && (r.push(y[n]), i.push(n)))
                    }
                    for (e = u.node().children, t = e.length, n = 0; n < t; n++) e[0].remove();
                    var s = r;
                    t = r.length, t > b && (t = b);
                    var p = [],
                        f = [];
                    for (n = 0; n < t; n++) {
                        for (var v = 1e6, g = 1e6, m = -1, x = 0; x < s.length; x++) {
                            o = s[x].toLowerCase();
                            var w = o.indexOf(a),
                                k = o.length;
                            w > -1 && w <= v && k <= g && (m = x, v = w, g = k)
                        }
                        p.push(s[m]), f.push(i[m]), s[m] = ""
                    }
                    for (t = r.length, t > b && (t = b), n = 0; n < t; n++) {
                        var C = document.createElement("li");
                        C.setAttribute("elementID", f[n]), C.onclick = c(f[n]), C.setAttribute("class", "dbEntry");
                        var S = document.createTextNode(p[n]);
                        C.appendChild(S), u.node().appendChild(C)
                    }
                }

                function s() {
                    if (x && n(), e.resetSearchHighlight(), 0 === y.length) return void console.log("dictionary is empty");
                    var t, o = u.node().children,
                        r = o.length;
                    if (h = d.node().value, 0 !== h.length) {
                        var i, a = [],
                            l = [],
                            s = h.toLowerCase();
                        for (t = 0; t < y.length; t++) {
                            var p = y[t];
                            void 0 !== p && (i = y[t].toLowerCase(), i.indexOf(s) > -1 && (a.push(y[t]), l.push(t)))
                        }
                        for (o = u.node().children, r = o.length, t = 0; t < r; t++) o[0].remove();
                        var f = a;
                        r = a.length, r > b && (r = b);
                        var v = [],
                            m = [];
                        for (t = 0; t < r; t++) {
                            for (var w = 1e8, k = 1e8, C = -1, S = 0; S < f.length; S++) {
                                i = f[S].toLowerCase();
                                var O = i.indexOf(s),
                                    E = i.length;
                                O > -1 && O <= w && E <= k && (C = S, w = O, k = E)
                            }
                            v.push(f[C]), m.push(l[C]), f[C] = ""
                        }
                        for (t = 0; t < r; t++) {
                            var A;
                            A = document.createElement("li"), A.setAttribute("elementID", m[t]), A.setAttribute("class", "dbEntry"), A.onclick = c(m[t]);
                            var I = document.createTextNode(v[t]);
                            A.appendChild(I), u.node().appendChild(A)
                        }
                        g.showSearchEntries()
                    } else
                        for (t = 0; t < r; t++) o[0].remove()
                }

                function c(t) {
                    return function() {
                        var n = t,
                            o = f[n],
                            r = m[n];
                        d.node().value = r, e.resetSearchHighlight(), e.highLightNodes(o), r !== h && l(), g.hideSearchEntries()
                    }
                }
                var d, u, p, f, v, h, g = {},
                    y = [],
                    m = [],
                    b = 6,
                    x = !0,
                    w = !1;
                return String.prototype.beginsWith = function(e) {
                    return 0 === this.indexOf(e)
                }, g.requestDictionaryUpdate = function() {
                    x = !0;
                    for (var e = u.node().children, t = e.length, n = 0; n < t; n++) e[0].remove();
                    d.node().value = ""
                }, g.setup = function() {
                    y = [], d = t.select("#search-input-text"), u = t.select("#searchEntryContainer"), d.on("input", s), d.on("keydown", a), d.on("click", r), d.on("mouseover", o)
                }, 
                g.hideSearchEntries = function() {
                    u.style("display", "none"), w = !1
                },
                g.showSearchEntries = function() {
                    u.style("display", "block"), w = !0
                }, g.clearText = function() {
                    d.node().value = "";
                    for (var e = u.node().children, t = e.length, n = 0; n < t; n++) e[0].remove()
                }, g
            }
        }).call(t, n(6))
    },
    325: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n() {
                    u.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    }), p.on("mouseover", function() {
                        var t = e.options().searchMenu();
                        t.hideSearchEntries()
                    }), u.on("click", function() {
                        var e, t, n;
                        if (1 !== c[0]) {
                            var o = c.indexOf(1) - 1,
                                l = c.indexOf(1);
                            for (e = l + 1; e < c.length; e++) c[e] = 0, s[e].style.display = "none";
                            for (c[o] = 1, s[o].style.display = "block", e = l + 1; e < c.length; e++) {
                                if (c[e] = 0, s[e].style.display = "block", t = s[o].getBoundingClientRect().top, n = s[e].getBoundingClientRect().top, t !== n) {
                                    s[e].style.display = "none", c[e] = 0;
                                    break
                                }
                                c[e] = 1
                            }
                            r();
                            var d = i(),
                                u = c.lastIndexOf(1);
                            d || (c[u] = 0, s[u].style.display = "none");
                            var p = c.lastIndexOf(1);
                            for (e = p - 1; e >= 0; e--) {
                                if (c[e] = 0, s[e].style.display = "block", t = s[o].getBoundingClientRect().top, n = s[e].getBoundingClientRect().top, t !== n) {
                                    s[e].style.display = "none", c[e] = 0;
                                    break
                                }
                                c[e] = 1
                            }
                            r(), d = i(), d || (u = c.indexOf(1), u !== -1 && (c[u] = 0, s[u].style.display = "none")), r(), d = i(), d || (u = c.indexOf(1), u !== -1 && (c[u] = 0, s[u].style.display = "none")), r(), d = i(), d || (u = c.indexOf(1), u !== -1 && (c[u] = 0, s[u].style.display = "none")), r(), a()
                        }
                    }), p.on("click", function() {
                        if (1 !== c[c.length - 1]) {
                            var e, t = c.lastIndexOf(1) + 1,
                                n = c.lastIndexOf(1);
                            for (e = n - 1; e >= 0; e--) c[e] = 0, s[e].style.display = "none";
                            for (c[t] = 1, s[t].style.display = "block", e = n - 1; e >= 0; e--) {
                                c[e] = 0, s[e].style.display = "block";
                                var o = s[t].getBoundingClientRect().top,
                                    l = s[e].getBoundingClientRect().top;
                                if (o !== l) {
                                    s[e].style.display = "none", c[e] = 0;
                                    break
                                }
                                c[e] = 1
                            }
                            r();
                            var d = i();
                            if (!d) {
                                var u = c.indexOf(1);
                                u !== -1 && (c[u] = 0, s[u].style.display = "none")
                            }
                            a()
                        }
                    })
                }

                function o() {
                    c[0] = 1, s[0].style.display = "block"
                }

                function r() {
                    var e = s.length - 2,
                        t = s.length - 1;
                    s[e].style.display = "block", s[t].style.display = "block", c.indexOf(0) !== -1 && (s[e].style.display = "block", s[t].style.display = "block")
                }

                function i() {
                    if (c.indexOf(0) === -1) return !0;
                    var e = s.length - 2,
                        t = s.length - 1,
                        n = c.indexOf(1);
                    n === -1 && (o(), n = c.indexOf(1));
                    var r = s[n].getBoundingClientRect().top,
                        i = s[e].getBoundingClientRect().top,
                        a = s[t].getBoundingClientRect().top;
                    s[e].style.display = "block", s[t].style.display = "block";
                    var l = !1;
                    return r === i && r === a && (l = !0), l
                }

                function a() {
                    1 !== c[c.length - 1] ? p.classed("highlighted", !0) : p.classed("highlighted", !1), 1 !== c[0] ? u.classed("highlighted", !0) : u.classed("highlighted", !1)
                }
                var l = {},
                    s = [],
                    c = [],
                    d = t.select("#optionsMenu"),
                    u = t.select("#LeftButton"),
                    p = t.select("#RightButton");
                return l.setup = function() {
                    var e, t = d.node().children;
                    for (e = 0; e < t.length; e++) s.push(t[e]);
                    for (n(), e = 0; e < s.length - 2; e++) s[e].style.display = "block", c[e] = 1
                }, l.updateVisibilityStatus = function() {
                    var e, t = c.indexOf(1);
                    t === -1 && (o(), t = c.indexOf(1));
                    var n, l = s[t].getBoundingClientRect().top;
                    for (e = 0; e < s.length - 2; e++) n = s[e].getBoundingClientRect().top, n === l ? c[e] = 1 : (c[e] = 0, s[e].style.display = "block");
                    var d = c.indexOf(1),
                        u = c.lastIndexOf(1);
                    for (d === -1 && u === -1 && (o(), d = c.indexOf(1), u = c.lastIndexOf(1)), e = d + 1; e < s.length - 2; e++) {
                        if (s[e].style.display = "block", l = s[d].getBoundingClientRect().top, n = s[e].getBoundingClientRect().top, l !== n) {
                            s[e].style.display = "block", c[e] = 0;
                            break
                        }
                        c[e] = 1
                    }
                    r();
                    var p, f = i();
                    if (f || 0 !== d || (p = c.lastIndexOf(1), p !== -1 && (c[p] = 0, s[p].style.display = "block")), 0 !== d || u !== c.length) {
                        if (u = c.lastIndexOf(1), u >= 1) {
                            for (e = u - 1; e >= 0; e--) c[e] = 0, s[e].style.display = "block";
                            for (e = u - 1; e >= 0; e--) {
                                if (c[e] = 0, s[e].style.display = "block", l = s[u].getBoundingClientRect().top, n = s[e].getBoundingClientRect().top, l !== n) {
                                    s[e].style.display = "block", c[e] = 0;
                                    break
                                }
                                c[e] = 1
                            }
                        }
                        r(), f = i(), f || (p = c.indexOf(1), p !== -1 && (c[p] = 0, s[p].style.display = "block"))
                    }
                    c.indexOf(1) === -1 && o(), a()
                }, l
            }
        }).call(t, n(6))
    },
    326: function(e, t, n) {
        (function(t) {
            e.exports = function(e) {
                function n() {
                    function e(e) {
                        e.classed("hidden", !0)
                    }

                    function n(e) {
                        e.classed("hidden", !1)
                    }
                    var o = t.selectAll(".accordion-trigger");
                    e(t.selectAll(".accordion-trigger:not(.accordion-trigger-active) + div")), o.on("click", function() {
                        var o = t.select(this),
                            r = t.selectAll(".accordion-trigger-active");
                        o.classed("accordion-trigger-active") ? (e(t.select(o.node().nextElementSibling)), o.classed("accordion-trigger-active", !1)) : (e(t.selectAll(".accordion-trigger-active + div")), r.classed("accordion-trigger-active", !1), n(t.select(o.node().nextElementSibling)), o.classed("accordion-trigger-active", !0))
                    })
                }

                function o(n) {
                    n = n || [], n.sort(function(e, t) {
                        return e === webvowl.util.constants().LANG_IRIBASED ? -1 : t === webvowl.util.constants().LANG_IRIBASED ? 1 : e === webvowl.util.constants().LANG_UNDEFINED ? -1 : t === webvowl.util.constants().LANG_UNDEFINED ? 1 : e.localeCompare(t)
                    });
                    var o = t.select("#language").on("change", function() {
                        e.language(t.event.target.value), i(), C.updateSelectionInformation(k)
                    });
                    o.selectAll("option").remove(), o.selectAll("option").data(n).enter().append("option").attr("value", function(e) {
                        return e
                    }).text(function(e) {
                        return e
                    }), r(o, n, "en") || r(o, n, webvowl.util.constants().LANG_UNDEFINED) || r(o, n, webvowl.util.constants().LANG_IRIBASED)
                }

                function r(t, n, o) {
                    var r = n.indexOf(o);
                    return r >= 0 && (t.property("selectedIndex", r), e.language(o), !0)
                }

                function i() {
                    var n = S.textInLanguage(w.title, e.language());
                    t.select("#title").text(n || "No title available"), t.select("#about").attr("href", w.iri).attr("target", "_blank").text(w.iri), t.select("#version").text(w.version || "--");
                    var o = w.author;
                    "string" == typeof o ? t.select("#authors").text(o) : o instanceof Array ? t.select("#authors").text(o.join(", ")) : t.select("#authors").text("--");
                    var r = S.textInLanguage(w.description, e.language());
                    t.select("#description").text(r || "No description available.")
                }

                function a(e, n) {
                    e = e || {}, t.select("#classCount").text(e.classCount || n.classCount()), t.select("#objectPropertyCount").text(e.objectPropertyCount || n.objectPropertyCount()), t.select("#datatypePropertyCount").text(e.datatypePropertyCount || n.datatypePropertyCount()), t.select("#individualCount").text(e.totalIndividualCount || n.totalIndividualCount()), t.select("#nodeCount").text(n.nodeCount()), t.select("#edgeCount").text(n.edgeCount())
                }

                function l(e) {
                    var n = t.select("#ontology-metadata");
                    n.selectAll("*").remove(), s(n, e), n.selectAll(".annotation").size() <= 0 && n.append("p").text("No annotations available.")
                }

                function s(e, n) {
                    n = n || {};
                    var o = [];
                    for (var r in n) n.hasOwnProperty(r) && o.push(n[r][0]);
                    e.selectAll(".annotation").remove(), e.selectAll(".annotation").data(o).enter().append("p").classed("annotation", !0).classed("statisticDetails", !0).text(function(e) {
                        return e.identifier + ":"
                    }).append("span").each(function(e) {
                        v(t.select(this), e.value, "iri" === e.type ? e.value : void 0)
                    })
                }

                function c() {
                    d(!1, !1, !0)
                }

                function d(e, n, o) {
                    t.select("#classSelectionInformation").classed("hidden", !e), t.select("#propertySelectionInformation").classed("hidden", !n), t.select("#noSelectionInformation").classed("hidden", !o)
                }

                function u(e) {
                    p(), f(t.select("#propname"), e.labelForCurrentLanguage(), e.iri()), t.select("#typeProp").text(e.type()), void 0 !== e.inverse() ? (t.select("#inverse").classed("hidden", !1), f(t.select("#inverse span"), e.inverse().labelForCurrentLanguage(), e.inverse().iri())) : t.select("#inverse").classed("hidden", !0);
                    var n = t.select("#propEquivUri");
                    b(n, e.equivalents()), b(t.select("#subproperties"), e.subproperties()), b(t.select("#superproperties"), e.superproperties()), void 0 !== e.minCardinality() ? (t.select("#infoCardinality").classed("hidden", !0), t.select("#minCardinality").classed("hidden", !1), t.select("#minCardinality span").text(e.minCardinality()), t.select("#maxCardinality").classed("hidden", !1), void 0 !== e.maxCardinality() ? t.select("#maxCardinality span").text(e.maxCardinality()) : t.select("#maxCardinality span").text("*")) : void 0 !== e.cardinality() ? (t.select("#minCardinality").classed("hidden", !0), t.select("#maxCardinality").classed("hidden", !0), t.select("#infoCardinality").classed("hidden", !1), t.select("#infoCardinality span").text(e.cardinality())) : (t.select("#infoCardinality").classed("hidden", !0), t.select("#minCardinality").classed("hidden", !0), t.select("#maxCardinality").classed("hidden", !0)), f(t.select("#domain"), e.domain().labelForCurrentLanguage(), e.domain().iri()), f(t.select("#range"), e.range().labelForCurrentLanguage(), e.range().iri()), h(e.attributes(), t.select("#propAttributes")), x(t.select("#propDescription"), e.descriptionForCurrentLanguage()), x(t.select("#propComment"), e.commentForCurrentLanguage()), s(t.select("#propertySelectionInformation"), e.annotations())
                }

                function p() {
                    d(!1, !0, !1)
                }

                function f(e, n, o) {
                    var r = t.select(e.node().parentNode);
                    n ? (e.selectAll("*").remove(), v(e, n, o), r.classed("hidden", !1)) : r.classed("hidden", !0)
                }

                function v(e, t, n) {
                    var o;
                    o = n ? e.append("a").attr("href", n).attr("title", n).attr("target", "_blank") : e.append("span"), o.text(t)
                }

                function h(e, n) {
                    var o = t.select(n.node().parentNode);
                    e && e.length > 0 && (g("object", e), g("datatype", e), g("rdf", e)), e && e.length > 0 ? (n.text(e.join(", ")), o.classed("hidden", !1)) : o.classed("hidden", !0)
                }

                function g(e, t) {
                    var n = t.indexOf(e);
                    n > -1 && t.splice(n, 1)
                }

                function y(e) {
                    m(), f(t.select("#name"), e.labelForCurrentLanguage(), e.iri());
                    var n = t.select("#classEquivUri");
                    b(n, e.equivalents()), t.select("#typeNode").text(e.type()), b(t.select("#individuals"), e.individuals());
                    var o = t.select("#disjointNodes"),
                        r = t.select(o.node().parentNode);
                    void 0 !== e.disjointWith() ? (o.selectAll("*").remove(), e.disjointWith().forEach(function(e, t) {
                        t > 0 && o.append("span").text(", "), v(o, e.labelForCurrentLanguage(), e.iri())
                    }), r.classed("hidden", !1)) : r.classed("hidden", !0), h(e.attributes(), t.select("#classAttributes")), x(t.select("#nodeDescription"), e.descriptionForCurrentLanguage()), x(t.select("#nodeComment"), e.commentForCurrentLanguage()), s(t.select("#classSelectionInformation"), e.annotations())
                }

                function m() {
                    d(!0, !1, !1)
                }

                function b(e, n) {
                    var o = t.select(e.node().parentNode);
                    n && n.length ? (e.selectAll("*").remove(), n.forEach(function(t, n) {
                        n > 0 && e.append("span").text(", "), v(e, t.labelForCurrentLanguage(), t.iri())
                    }), o.classed("hidden", !1)) : o.classed("hidden", !0)
                }

                function x(e, n) {
                    var o = t.select(e.node().parentNode),
                        r = !!n;
                    n && e.text(n), o.classed("hidden", !r)
                }
                var w, k, C = {},
                    S = webvowl.util.languageTools(),
                    O = webvowl.util.elementTools();
                return C.setup = function() {
                    n()
                }, C.clearOntologyInformation = function() {
                    t.select("#title").text("No title available"), t.select("#about").attr("href", "#").attr("target", "_blank").text("not given"), t.select("#version").text("--"), t.select("#authors").text("--"), t.select("#description").text("No description available.");
                    var e = t.select("#ontology-metadata");
                    e.selectAll("*").remove(), t.select("#classCount").text("0"), t.select("#objectPropertyCount").text("0"), t.select("#datatypePropertyCount").text("0"), t.select("#individualCount").text("0"), t.select("#nodeCount").text("0"), t.select("#edgeCount").text("0");
                    var n = t.select("#selection-details-trigger").classed("accordion-trigger-active");
                    n && t.select("#selection-details-trigger").node().click(), c()
                }, C.updateOntologyInformation = function(e, t) {
                    e = e || {}, w = e.header || {}, i(), a(e.metrics, t), l(w.other), C.updateSelectionInformation(void 0), o(w.languages)
                }, C.updateSelectionInformation = function(e) {
                    if (k = e, !t.event || !t.event.defaultPrevented) {
                        var n = t.select("#selection-details-trigger").classed("accordion-trigger-active");
                        if (e && !n) t.select("#selection-details-trigger").node().click();
                        else if (!e && n) return void c();
                        O.isProperty(e) ? u(e) : O.isNode(e) && y(e)
                    }
                }, C
            }
        }).call(t, n(6))
    }
});
