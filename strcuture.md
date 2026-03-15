# File Tree: learnalytics

**Generated:** 3/15/2026, 8:24:26 PM
**Root Path:** `d:\projects\learnalytics`

```
├── 📁 authentication
│   ├── 📁 migrations
│   │   └── 🐍 __init__.py
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   └── 🐍 views.py
├── 📁 feedback
│   ├── 📁 migrations
│   │   ├── 🐍 0001_initial.py
│   │   ├── 🐍 0002_feedback_description.py
│   │   └── 🐍 __init__.py
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
│   └── 🐍 views.py
├── 📁 learnalytics
│   ├── 🐍 __init__.py
│   ├── 🐍 asgi.py
│   ├── 🐍 settings.py
│   ├── 🐍 urls.py
│   └── 🐍 wsgi.py
├── 📁 performance
│   ├── 📁 migrations
│   │   └── 🐍 __init__.py
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 utils.py
│   └── 🐍 views.py
├── 📁 static
│   └── 📁 css
│       ├── 🎨 admin_login.css
│       ├── 🎨 admin_shell.css
│       ├── 🎨 home.css
│       ├── 🎨 index.css
│       └── 🎨 teacher.css
├── 📁 staticfiles
│   ├── 📁 admin
│   │   ├── 📁 css
│   │   │   ├── 📁 vendor
│   │   │   │   └── 📁 select2
│   │   │   │       ├── 📝 LICENSE-SELECT2.md
│   │   │   │       └── 🎨 select2.css
│   │   │   ├── 🎨 autocomplete.css
│   │   │   ├── 🎨 base.css
│   │   │   ├── 🎨 changelists.css
│   │   │   ├── 🎨 dark_mode.css
│   │   │   ├── 🎨 dashboard.css
│   │   │   ├── 🎨 forms.css
│   │   │   ├── 🎨 login.css
│   │   │   ├── 🎨 nav_sidebar.css
│   │   │   ├── 🎨 responsive.css
│   │   │   ├── 🎨 responsive_rtl.css
│   │   │   ├── 🎨 rtl.css
│   │   │   ├── 🎨 unusable_password_field.css
│   │   │   └── 🎨 widgets.css
│   │   ├── 📁 img
│   │   │   ├── 📝 README.md
│   │   │   ├── 🖼️ calendar-icons.svg
│   │   │   ├── 🖼️ icon-addlink.svg
│   │   │   ├── 🖼️ icon-alert-dark.svg
│   │   │   ├── 🖼️ icon-alert.svg
│   │   │   ├── 🖼️ icon-calendar.svg
│   │   │   ├── 🖼️ icon-changelink.svg
│   │   │   ├── 🖼️ icon-clock.svg
│   │   │   ├── 🖼️ icon-debug-dark.svg
│   │   │   ├── 🖼️ icon-debug.svg
│   │   │   ├── 🖼️ icon-deletelink.svg
│   │   │   ├── 🖼️ icon-hidelink.svg
│   │   │   ├── 🖼️ icon-info-dark.svg
│   │   │   ├── 🖼️ icon-info.svg
│   │   │   ├── 🖼️ icon-no-dark.svg
│   │   │   ├── 🖼️ icon-no.svg
│   │   │   ├── 🖼️ icon-unknown-alt.svg
│   │   │   ├── 🖼️ icon-unknown.svg
│   │   │   ├── 🖼️ icon-viewlink.svg
│   │   │   ├── 🖼️ icon-yes-dark.svg
│   │   │   ├── 🖼️ icon-yes.svg
│   │   │   ├── 🖼️ inline-delete.svg
│   │   │   ├── 🖼️ search.svg
│   │   │   ├── 🖼️ selector-icons.svg
│   │   │   ├── 🖼️ sorting-icons.svg
│   │   │   ├── 🖼️ tooltag-add.svg
│   │   │   └── 🖼️ tooltag-arrowright.svg
│   │   └── 📁 js
│   │       ├── 📁 admin
│   │       │   ├── 📄 DateTimeShortcuts.js
│   │       │   └── 📄 RelatedObjectLookups.js
│   │       ├── 📁 vendor
│   │       │   ├── 📁 jquery
│   │       │   │   ├── 📄 LICENSE.txt
│   │       │   │   └── 📄 jquery.js
│   │       │   ├── 📁 select2
│   │       │   │   ├── 📁 i18n
│   │       │   │   │   ├── 📄 af.js
│   │       │   │   │   ├── 📄 ar.js
│   │       │   │   │   ├── 📄 az.js
│   │       │   │   │   ├── 📄 bg.js
│   │       │   │   │   ├── 📄 bn.js
│   │       │   │   │   ├── 📄 bs.js
│   │       │   │   │   ├── 📄 ca.js
│   │       │   │   │   ├── 📄 cs.js
│   │       │   │   │   ├── 📄 da.js
│   │       │   │   │   ├── 📄 de.js
│   │       │   │   │   ├── 📄 dsb.js
│   │       │   │   │   ├── 📄 el.js
│   │       │   │   │   ├── 📄 en.js
│   │       │   │   │   ├── 📄 es.js
│   │       │   │   │   ├── 📄 et.js
│   │       │   │   │   ├── 📄 eu.js
│   │       │   │   │   ├── 📄 fa.js
│   │       │   │   │   ├── 📄 fi.js
│   │       │   │   │   ├── 📄 fr.js
│   │       │   │   │   ├── 📄 gl.js
│   │       │   │   │   ├── 📄 he.js
│   │       │   │   │   ├── 📄 hi.js
│   │       │   │   │   ├── 📄 hr.js
│   │       │   │   │   ├── 📄 hsb.js
│   │       │   │   │   ├── 📄 hu.js
│   │       │   │   │   ├── 📄 hy.js
│   │       │   │   │   ├── 📄 id.js
│   │       │   │   │   ├── 📄 is.js
│   │       │   │   │   ├── 📄 it.js
│   │       │   │   │   ├── 📄 ja.js
│   │       │   │   │   ├── 📄 ka.js
│   │       │   │   │   ├── 📄 km.js
│   │       │   │   │   ├── 📄 ko.js
│   │       │   │   │   ├── 📄 lt.js
│   │       │   │   │   ├── 📄 lv.js
│   │       │   │   │   ├── 📄 mk.js
│   │       │   │   │   ├── 📄 ms.js
│   │       │   │   │   ├── 📄 nb.js
│   │       │   │   │   ├── 📄 ne.js
│   │       │   │   │   ├── 📄 nl.js
│   │       │   │   │   ├── 📄 pl.js
│   │       │   │   │   ├── 📄 ps.js
│   │       │   │   │   ├── 📄 pt-BR.js
│   │       │   │   │   ├── 📄 pt.js
│   │       │   │   │   ├── 📄 ro.js
│   │       │   │   │   ├── 📄 ru.js
│   │       │   │   │   ├── 📄 sk.js
│   │       │   │   │   ├── 📄 sl.js
│   │       │   │   │   ├── 📄 sq.js
│   │       │   │   │   ├── 📄 sr-Cyrl.js
│   │       │   │   │   ├── 📄 sr.js
│   │       │   │   │   ├── 📄 sv.js
│   │       │   │   │   ├── 📄 th.js
│   │       │   │   │   ├── 📄 tk.js
│   │       │   │   │   ├── 📄 tr.js
│   │       │   │   │   ├── 📄 uk.js
│   │       │   │   │   ├── 📄 vi.js
│   │       │   │   │   ├── 📄 zh-CN.js
│   │       │   │   │   └── 📄 zh-TW.js
│   │       │   │   ├── 📝 LICENSE.md
│   │       │   │   └── 📄 select2.full.js
│   │       │   └── 📁 xregexp
│   │       │       ├── 📄 LICENSE.txt
│   │       │       └── 📄 xregexp.js
│   │       ├── 📄 SelectBox.js
│   │       ├── 📄 SelectFilter2.js
│   │       ├── 📄 actions.js
│   │       ├── 📄 autocomplete.js
│   │       ├── 📄 calendar.js
│   │       ├── 📄 cancel.js
│   │       ├── 📄 change_form.js
│   │       ├── 📄 core.js
│   │       ├── 📄 filters.js
│   │       ├── 📄 inlines.js
│   │       ├── 📄 jquery.init.js
│   │       ├── 📄 nav_sidebar.js
│   │       ├── 📄 popup_response.js
│   │       ├── 📄 prepopulate.js
│   │       ├── 📄 prepopulate_init.js
│   │       ├── 📄 theme.js
│   │       └── 📄 urlify.js
│   ├── 📁 css
│   │   ├── 🎨 admin_login.css
│   │   ├── 🎨 home.css
│   │   └── 🎨 teacher.css
│   ├── 📁 jazzmin
│   │   ├── 📁 css
│   │   │   └── 🎨 main.css
│   │   ├── 📁 img
│   │   │   ├── 🖼️ calendar-icons.svg
│   │   │   ├── 🖼️ default-log.svg
│   │   │   ├── 🖼️ default.jpg
│   │   │   ├── 🖼️ icon-calendar.svg
│   │   │   ├── 🖼️ icon-changelink.svg
│   │   │   └── 🖼️ selector-icons.svg
│   │   ├── 📁 js
│   │   │   ├── 📄 change_form.js
│   │   │   ├── 📄 change_list.js
│   │   │   ├── 📄 main.js
│   │   │   ├── 📄 related-modal.js
│   │   │   └── 📄 ui-builder.js
│   │   └── 📁 plugins
│   │       └── 📁 bootstrap-show-modal
│   ├── 📁 rest_framework
│   │   ├── 📁 css
│   │   │   ├── 🎨 bootstrap-tweaks.css
│   │   │   ├── 🎨 default.css
│   │   │   ├── 🎨 font-awesome-4.0.3.css
│   │   │   └── 🎨 prettify.css
│   │   ├── 📁 docs
│   │   │   ├── 📁 css
│   │   │   │   ├── 🎨 base.css
│   │   │   │   └── 🎨 highlight.css
│   │   │   ├── 📁 img
│   │   │   │   ├── 📄 favicon.ico
│   │   │   │   └── 🖼️ grid.png
│   │   │   └── 📁 js
│   │   │       ├── 📄 api.js
│   │   │       └── 📄 highlight.pack.js
│   │   ├── 📁 fonts
│   │   │   ├── 📄 fontawesome-webfont.eot
│   │   │   ├── 🖼️ fontawesome-webfont.svg
│   │   │   ├── 📄 fontawesome-webfont.ttf
│   │   │   ├── 📄 fontawesome-webfont.woff
│   │   │   ├── 📄 glyphicons-halflings-regular.eot
│   │   │   ├── 🖼️ glyphicons-halflings-regular.svg
│   │   │   ├── 📄 glyphicons-halflings-regular.ttf
│   │   │   ├── 📄 glyphicons-halflings-regular.woff
│   │   │   └── 📄 glyphicons-halflings-regular.woff2
│   │   ├── 📁 img
│   │   │   ├── 🖼️ glyphicons-halflings-white.png
│   │   │   ├── 🖼️ glyphicons-halflings.png
│   │   │   └── 🖼️ grid.png
│   │   └── 📁 js
│   │       ├── 📄 ajax-form.js
│   │       ├── 📄 coreapi-0.1.1.js
│   │       ├── 📄 csrf.js
│   │       ├── 📄 default.js
│   │       ├── 📄 load-ajax-form.js
│   │       └── 📄 prettify-min.js
│   └── 📁 vendor
│       ├── 📁 adminlte
│       │   ├── 📁 css
│       │   ├── 📁 img
│       │   │   ├── 🖼️ AdminLTELogo.png
│       │   │   ├── 🖼️ icons.png
│       │   │   └── 🖼️ user2-160x160.jpg
│       │   └── 📁 js
│       ├── 📁 bootstrap
│       │   └── 📁 js
│       ├── 📁 bootswatch
│       │   ├── 📁 cerulean
│       │   ├── 📁 cosmo
│       │   ├── 📁 cyborg
│       │   ├── 📁 darkly
│       │   ├── 📁 default
│       │   ├── 📁 flatly
│       │   ├── 📁 journal
│       │   ├── 📁 litera
│       │   ├── 📁 lumen
│       │   ├── 📁 lux
│       │   ├── 📁 materia
│       │   ├── 📁 minty
│       │   ├── 📁 morph
│       │   ├── 📁 pulse
│       │   ├── 📁 quartz
│       │   ├── 📁 sandstone
│       │   ├── 📁 simplex
│       │   ├── 📁 sketchy
│       │   ├── 📁 slate
│       │   ├── 📁 solar
│       │   ├── 📁 spacelab
│       │   ├── 📁 superhero
│       │   ├── 📁 united
│       │   ├── 📁 vapor
│       │   ├── 📁 yeti
│       │   └── 📁 zephyr
│       ├── 📁 fontawesome-free
│       │   ├── 📁 css
│       │   └── 📁 webfonts
│       │       ├── 📄 fa-brands-400.ttf
│       │       ├── 📄 fa-brands-400.woff2
│       │       ├── 📄 fa-regular-400.ttf
│       │       ├── 📄 fa-regular-400.woff2
│       │       ├── 📄 fa-solid-900.ttf
│       │       ├── 📄 fa-solid-900.woff2
│       │       ├── 📄 fa-v4compatibility.ttf
│       │       └── 📄 fa-v4compatibility.woff2
│       └── 📁 select2
│           ├── 📁 css
│           └── 📁 js
├── 📁 students
│   ├── 📁 ai
│   │   ├── 🐍 analytics.py
│   │   ├── 🐍 predictor.py
│   │   ├── 🐍 recommender.py
│   │   └── 🐍 training.py
│   ├── 📁 migrations
│   │   ├── 🐍 0001_initial.py
│   │   ├── 🐍 0002_alter_student_options_mark_exam_date_and_more.py
│   │   └── 🐍 __init__.py
│   ├── 📁 services
│   │   └── 🐍 student_service.py
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
│   └── 🐍 views.py
├── 📁 teacher
│   ├── 📁 migrations
│   │   └── 🐍 __init__.py
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
│   └── 🐍 views.py
├── 📁 templates
│   ├── 📁 admin
│   │   ├── 🌐 base.html
│   │   ├── 🌐 index.html
│   │   └── 🌐 login.html
│   ├── 🌐 dashboard.html
│   ├── 🌐 feedback_form.html
│   ├── 🌐 home.html
│   └── 🌐 success.html
├── 📁 visualization
│   ├── 📁 migrations
│   │   └── 🐍 __init__.py
│   ├── 🐍 __init__.py
│   ├── 🐍 admin.py
│   ├── 🐍 apps.py
│   ├── 🐍 models.py
│   ├── 🐍 tests.py
│   ├── 🐍 urls.py
│   └── 🐍 views.py
├── 📝 LICENSE.md
├── 📄 db.sqlite3
├── 🐍 manage.py
├── 📝 readme.md
└── 📄 requirements.txt
```

---
*Generated by FileTree Pro Extension*