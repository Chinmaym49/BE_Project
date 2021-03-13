var customIcon = document.createElement('img');
customIcon.src = '/static/img/deltag.svg';

var arr=Array()

var autocomplete = new SelectPure(".autocomplete-select", {
    multiple: true,
    autocomplete: true,
    inlineIcon: customIcon,
    onChange: value => { arr=value; },
    classNames: {
        select: "select-pure__select",
        dropdownShown: "select-pure__select--opened",
        multiselect: "select-pure__select--multiple",
        label: "select-pure__label",
        placeholder: "select-pure__placeholder",
        dropdown: "select-pure__options",
        option: "select-pure__option",
        autocompleteInput: "select-pure__autocomplete",
        selectedLabel: "select-pure__selected-label",
        selectedOption: "select-pure__option--selected",
        placeholderHidden: "select-pure__placeholder--hidden",
        optionHidden: "select-pure__option--hidden",
    },
    options: [	
        {label:'c-hash',value:'c-hash'},{label:'java',value:'java'},{label:'php',value:'php'},{label:'javascript',value:'javascript'},{label:'android',value:'android'},{label:'jquery',value:'jquery'},{label:'c++',value:'c++'},{label:'asp.net',value:'asp.net'},{label:'html',value:'html'},{label:'.net',value:'.net'},{label:'iphone',value:'iphone'},{label:'python',value:'python'},{label:'mysql',value:'mysql'},{label:'sql',value:'sql'},{label:'objective-c',value:'objective-c'},{label:'ios',value:'ios'},{label:'css',value:'css'},{label:'ruby-on-rails',value:'ruby-on-rails'},{label:'windows',value:'windows'},{label:'linux',value:'linux'},{label:'c',value:'c'},{label:'wpf',value:'wpf'},{label:'arrays',value:'arrays'},{label:'sql-server',value:'sql-server'},{label:'asp.net-mvc',value:'asp.net-mvc'},{label:'database',value:'database'},{label:'ajax',value:'ajax'},{label:'xml',value:'xml'},{label:'ruby',value:'ruby'},{label:'eclipse',value:'eclipse'},{label:'xcode',value:'xcode'},{label:'django',value:'django'},{label:'vb.net',value:'vb.net'},{label:'facebook',value:'facebook'},{label:'json',value:'json'},{label:'winforms',value:'winforms'},{label:'html5',value:'html5'},{label:'homework',value:'homework'},{label:'regex',value:'regex'},{label:'asp.net-mvc-3',value:'asp.net-mvc-3'},{label:'bash',value:'bash'},{label:'performance',value:'performance'},{label:'osx',value:'osx'},{label:'forms',value:'forms'},{label:'ruby-on-rails-3',value:'ruby-on-rails-3'},{label:'string',value:'string'},{label:'visual-studio-2010',value:'visual-studio-2010'},{label:'multithreading',value:'multithreading'},{label:'visual-studio',value:'visual-studio'},{label:'algorithm',value:'algorithm'},{label:'web-services',value:'web-services'},{label:'actionscript-3',value:'actionscript-3'},{label:'git',value:'git'},{label:'excel',value:'excel'},{label:'silverlight',value:'silverlight'},{label:'hibernate',value:'hibernate'},{label:'spring',value:'spring'},{label:'apache',value:'apache'},{label:'image',value:'image'},{label:'windows-7',value:'windows-7'},{label:'oracle',value:'oracle'},
        {label:'security',value:'security'},{label:'query',value:'query'},{label:'wcf',value:'wcf'},{label:'.htaccess',value:'.htaccess'},{label:'flash',value:'flash'},{label:'linq',value:'linq'},{label:'file',value:'file'},{label:'cocoa-touch',value:'cocoa-touch'},{label:'sqlite',value:'sqlite'},{label:'networking',value:'networking'},{label:'sql-server-2008',value:'sql-server-2008'},{label:'ubuntu',value:'ubuntu'},{label:'oop',value:'oop'},{label:'entity-framework',value:'entity-framework'},{label:'ipad',value:'ipad'},{label:'class',value:'class'},{label:'google-chrome',value:'google-chrome'},{label:'perl',value:'perl'},{label:'api',value:'api'},{label:'codeigniter',value:'codeigniter'},{label:'shell',value:'shell'},{label:'list',value:'list'},{label:'wordpress',value:'wordpress'},{label:'jsp',value:'jsp'},{label:'http',value:'http'},{label:'iis',value:'iis'},{label:'uitableview',value:'uitableview'},{label:'flex',value:'flex'},{label:'jsf',value:'jsf'},{label:'internet-explorer',value:'internet-explorer'},{label:'jquery-ui',value:'jquery-ui'},{label:'vba',value:'vba'},{label:'linear-algebra',value:'linear-algebra'},{label:'apache2',value:'apache2'},{label:'function',value:'function'},{label:'google-maps',value:'google-maps'},{label:'mvc',value:'mvc'},{label:'email',value:'email'},{label:'xaml',value:'xaml'},{label:'design',value:'design'},{label:'generics',value:'generics'},{label:'validation',value:'validation'},{label:'real-analysis',value:'real-analysis'},{label:'firefox',value:'firefox'},{label:'debugging',value:'debugging'},{label:'tsql',value:'tsql'},{label:'unix',value:'unix'},{label:'matlab',value:'matlab'},{label:'cocoa',value:'cocoa'},{label:'postgresql',value:'postgresql'},{label:'sql-server-2005',value:'sql-server-2005'},{label:'r',value:'r'},{label:'date',value:'date'},{label:'google-app-engine',value:'google-app-engine'},{label:'calculus',value:'calculus'},{label:'parsing',value:'parsing'},{label:'sockets',value:'sockets'},{label:'visual-c++',value:'visual-c++'},{label:'winapi',value:'winapi'},{label:'command-line',value:'command-line'},
        {label:'exception',value:'exception'},{label:'url',value:'url'},{label:'jquery-ajax',value:'jquery-ajax'},{label:'session',value:'session'},{label:'mod-rewrite',value:'mod-rewrite'},{label:'svn',value:'svn'},{label:'loops',value:'loops'},{label:'visual-studio-2008',value:'visual-studio-2008'},{label:'design-patterns',value:'design-patterns'},{label:'object',value:'object'},{label:'datetime',value:'datetime'},{label:'unit-testing',value:'unit-testing'},{label:'sharepoint',value:'sharepoint'},{label:'c#-4.0',value:'c#-4.0'},{label:'rest',value:'rest'},{label:'data-binding',value:'data-binding'},{label:'sorting',value:'sorting'},{label:'magento',value:'magento'},{label:'variables',value:'variables'},{label:'templates',value:'templates'},{label:'dom',value:'dom'},{label:'table',value:'table'},{label:'search',value:'search'},{label:'cakephp',value:'cakephp'},{label:'pointers',value:'pointers'},{label:'redirect',value:'redirect'},{label:'powershell',value:'powershell'},{label:'windows-phone-7',value:'windows-phone-7'},{label:'node.js',value:'node.js'},{label:'tomcat',value:'tomcat'},{label:'web-applications',value:'web-applications'},{label:'optimization',value:'optimization'},{label:'swing',value:'swing'},{label:'servlets',value:'servlets'},{label:'qt',value:'qt'},{label:'authentication',value:'authentication'},{label:'android-layout',value:'android-layout'},{label:'events',value:'events'},{label:'jquery-mobile',value:'jquery-mobile'},{label:'caching',value:'caching'},{label:'listview',value:'listview'},{label:'probability',value:'probability'},{label:'memory',value:'memory'},{label:'zend-framework',value:'zend-framework'},{label:'java-ee',value:'java-ee'},{label:'css3',value:'css3'},{label:'inheritance',value:'inheritance'},{label:'gwt',value:'gwt'},{label:'xslt',value:'xslt'},{label:'math',value:'math'},{label:'facebook-graph-api',value:'facebook-graph-api'},{label:'stored-procedures',value:'stored-procedures'},{label:'gui',value:'gui'},{label:'ms-access',value:'ms-access'},{label:'linq-to-sql',value:'linq-to-sql'},{label:'iis7',value:'iis7'},
        {label:'post',value:'post'},{label:'reflection',value:'reflection'},{label:'phonegap',value:'phonegap'},{label:'mobile',value:'mobile'},{label:'grails',value:'grails'},{label:'activerecord',value:'activerecord'},{label:'file-upload',value:'file-upload'},{label:'razor',value:'razor'},{label:'browser',value:'browser'},{label:'gridview',value:'gridview'},{label:'delphi',value:'delphi'},{label:'google',value:'google'},{label:'csv',value:'csv'},{label:'testing',value:'testing'},{label:'database-design',value:'database-design'},{label:'memory-management',value:'memory-management'},{label:'vim',value:'vim'},{label:'select',value:'select'},{label:'animation',value:'animation'},{label:'ssl',value:'ssl'},{label:'ssh',value:'ssh'},{label:'ios5',value:'ios5'},{label:'cookies',value:'cookies'},{label:'scala',value:'scala'},{label:'iframe',value:'iframe'},{label:'logging',value:'logging'},{label:'pdf',value:'pdf'},{label:'blackberry',value:'blackberry'},{label:'curl',value:'curl'},{label:'mongodb',value:'mongodb'},{label:'layout',value:'layout'},{label:'asp.net-mvc-2',value:'asp.net-mvc-2'},{label:'file-io',value:'file-io'},{label:'spring-mvc',value:'spring-mvc'},{label:'plugins',value:'plugins'},{label:'excel-vba',value:'excel-vba'},{label:'mvvm',value:'mvvm'},{label:'serialization',value:'serialization'},{label:'drop-down-menu',value:'drop-down-menu'},{label:'application',value:'application'},{label:'windows-xp',value:'windows-xp'},{label:'nhibernate',value:'nhibernate'},{label:'core-data',value:'core-data'},{label:'windows-server-2008',value:'windows-server-2008'},{label:'jquery-plugins',value:'jquery-plugins'},{label:'jsf-2',value:'jsf-2'},{label:'asp-classic',value:'asp-classic'},{label:'dynamic',value:'dynamic'},{label:'user-interface',value:'user-interface'},{label:'data-structures',value:'data-structures'},{label:'dns',value:'dns'},{label:'maven',value:'maven'},{label:'opencv',value:'opencv'},{label:'netbeans',value:'netbeans'},{label:'scripting',value:'scripting'},{label:'collections',value:'collections'},{label:'unicode',value:'unicode'},
        {label:'script',value:'script'},{label:'javascript-events',value:'javascript-events'},{label:'encoding',value:'encoding'},{label:'button',value:'button'},{label:'printing',value:'printing'},{label:'version-control',value:'version-control'},{label:'join',value:'join'},{label:'xpath',value:'xpath'},{label:'google-maps-api-3',value:'google-maps-api-3'},{label:'permissions',value:'permissions'},{label:'abstract-algebra',value:'abstract-algebra'},{label:'android-intent',value:'android-intent'},{label:'multidimensional-array',value:'multidimensional-array'},{label:'haskell',value:'haskell'},{label:'active-directory',value:'active-directory'},{label:'nginx',value:'nginx'},{label:'syntax',value:'syntax'},{label:'datagridview',value:'datagridview'},{label:'div',value:'div'},{label:'random',value:'random'},{label:'web',value:'web'},{label:'iphone-sdk-4.0',value:'iphone-sdk-4.0'},{label:'opengl',value:'opengl'},{label:'twitter-bootstrap',value:'twitter-bootstrap'},{label:'canvas',value:'canvas'},{label:'login',value:'login'},{label:'jdbc',value:'jdbc'},{label:'image-processing',value:'image-processing'},{label:'jpa',value:'jpa'},{label:'dictionary',value:'dictionary'},{label:'ant',value:'ant'},{label:'if-statement',value:'if-statement'},{label:'binding',value:'binding'},{label:'twitter',value:'twitter'},{label:'backbone.js',value:'backbone.js'},{label:'jqgrid',value:'jqgrid'},{label:'architecture',value:'architecture'},{label:'audio',value:'audio'},{label:'sequences-and-series',value:'sequences-and-series'},{label:'complex-analysis',value:'complex-analysis'},{label:'geometry',value:'geometry'},{label:'general-topology',value:'general-topology'},{label:'uitableviewcell',value:'uitableviewcell'},{label:'jquery-selectors',value:'jquery-selectors'},{label:'heroku',value:'heroku'},{label:'ftp',value:'ftp'},{label:'extjs',value:'extjs'},{label:'time',value:'time'},{label:'soap',value:'soap'},{label:'combinatorics',value:'combinatorics'},{label:'asp.net-mvc-4',value:'asp.net-mvc-4'},{label:'exception-handling',value:'exception-handling'},
        {label:'for-loop',value:'for-loop'},{label:'pdo',value:'pdo'},{label:'dll',value:'dll'},{label:'statistics',value:'statistics'},{label:'encryption',value:'encryption'},{label:'sharepoint2010',value:'sharepoint2010'},{label:'sqlite3',value:'sqlite3'},{label:'drupal',value:'drupal'},{label:'url-rewriting',value:'url-rewriting'},{label:'ado.net',value:'ado.net'},{label:'algebra-precalculus',value:'algebra-precalculus'},{label:'emacs',value:'emacs'},{label:'google-chrome-extension',value:'google-chrome-extension'},{label:'group-theory',value:'group-theory'},{label:'deployment',value:'deployment'},{label:'entity-framework-4',value:'entity-framework-4'},{label:'uiwebview',value:'uiwebview'},{label:'actionscript',value:'actionscript'},{label:'primefaces',value:'primefaces'},{label:'struts2',value:'struts2'},{label:'character-encoding',value:'character-encoding'},{label:'service',value:'service'},{label:'vbscript',value:'vbscript'},{label:'checkbox',value:'checkbox'},{label:'knockout.js',value:'knockout.js'},{label:'matrices',value:'matrices'},{label:'autocomplete',value:'autocomplete'},{label:'datagrid',value:'datagrid'},{label:'video',value:'video'},{label:'graphics',value:'graphics'},{label:'text',value:'text'},{label:'utf-8',value:'utf-8'},{label:'amazon-ec2',value:'amazon-ec2'},{label:'methods',value:'methods'},{label:'configuration',value:'configuration'},{label:'types',value:'types'},{label:'xhtml',value:'xhtml'},{label:'analysis',value:'analysis'},{label:'recursion',value:'recursion'},{label:'android-emulator',value:'android-emulator'},{label:'language-agnostic',value:'language-agnostic'},{label:'macros',value:'macros'},{label:'https',value:'https'},{label:'github',value:'github'},{label:'usercontrols',value:'usercontrols'},{label:'properties',value:'properties'},{label:'.net-4.0',value:'.net-4.0'},{label:'php5',value:'php5'},{label:'batch',value:'batch'},{label:'upload',value:'upload'},{label:'batch-file',value:'batch-file'},{label:'stl',value:'stl'},{label:'error-handling',value:'error-handling'},{label:'input',value:'input'},
        {label:'data',value:'data'},{label:'groovy',value:'groovy'},{label:'joomla',value:'joomla'},{label:'xcode4',value:'xcode4'},{label:'foreach',value:'foreach'},{label:'silverlight-4.0',value:'silverlight-4.0'},{label:'django-models',value:'django-models'},{label:'arraylist',value:'arraylist'},{label:'hash',value:'hash'},{label:'coding-style',value:'coding-style'},{label:'mfc',value:'mfc'},{label:'interface',value:'interface'},{label:'vector',value:'vector'},{label:'opengl-es',value:'opengl-es'},{label:'symfony2',value:'symfony2'},{label:'gcc',value:'gcc'},{label:'boost',value:'boost'},{label:'asynchronous',value:'asynchronous'},{label:'combobox',value:'combobox'},{label:'triggers',value:'triggers'},{label:'fonts',value:'fonts'},{label:'casting',value:'casting'},{label:'routing',value:'routing'},{label:'frameworks',value:'frameworks'},{label:'orm',value:'orm'},{label:'localization',value:'localization'},{label:'coldfusion',value:'coldfusion'},{label:'plsql',value:'plsql'},{label:'website',value:'website'},{label:'cron',value:'cron'},{label:'python-3.x',value:'python-3.x'},{label:'limit',value:'limit'},{label:'python-2.7',value:'python-2.7'},{label:'memory-leaks',value:'memory-leaks'},{label:'proxy',value:'proxy'},{label:'uiview',value:'uiview'},{label:'centos',value:'centos'},{label:'view',value:'view'},{label:'tcp',value:'tcp'},{label:'vb6',value:'vb6'},{label:'sdk',value:'sdk'},{label:'internet-explorer-8',value:'internet-explorer-8'},{label:'calendar',value:'calendar'},{label:'azure',value:'azure'},{label:'windows-8',value:'windows-8'},{label:'terminal',value:'terminal'},{label:'webview',value:'webview'},{label:'.net-3.5',value:'.net-3.5'},{label:'insert',value:'insert'},{label:'graph',value:'graph'},{label:'activity',value:'activity'},{label:'map',value:'map'},{label:'menu',value:'menu'},{label:'webserver',value:'webserver'},{label:'reporting-services',value:'reporting-services'},{label:'ruby-on-rails-3.1',value:'ruby-on-rails-3.1'},{label:'concurrency',value:'concurrency'},{label:'reference',value:'reference'},
        {label:'programming-languages',value:'programming-languages'},{label:'sed',value:'sed'},{label:'timer',value:'timer'},{label:'textbox',value:'textbox'},{label:'installation',value:'installation'},{label:'parameters',value:'parameters'},{label:'backup',value:'backup'},{label:'process',value:'process'},{label:'compiler',value:'compiler'},{label:'filesystems',value:'filesystems'},{label:'constructor',value:'constructor'},{label:'model',value:'model'},{label:'import',value:'import'},{label:'air',value:'air'},{label:'junit',value:'junit'},{label:'clojure',value:'clojure'},{label:'io',value:'io'},{label:'static',value:'static'},{label:'internationalization',value:'internationalization'},{label:'ide',value:'ide'},{label:'tabs',value:'tabs'},{label:'numpy',value:'numpy'},{label:'windows-server-2003',value:'windows-server-2003'},{label:'selenium',value:'selenium'},{label:'safari',value:'safari'},{label:'amazon-web-services',value:'amazon-web-services'},{label:'java-me',value:'java-me'},{label:'uiviewcontroller',value:'uiviewcontroller'},{label:'mercurial',value:'mercurial'},{label:'visual-studio-2012',value:'visual-studio-2012'},{label:'matrix',value:'matrix'},{label:'number-theory',value:'number-theory'},{label:'struct',value:'struct'},{label:'hyperlink',value:'hyperlink'},{label:'uiscrollview',value:'uiscrollview'},{label:'svg',value:'svg'},{label:'debian',value:'debian'},{label:'resources',value:'resources'},{label:'attributes',value:'attributes'},{label:'keyboard',value:'keyboard'},{label:'youtube',value:'youtube'},{label:'delete',value:'delete'},{label:'dojo',value:'dojo'},{label:'rss',value:'rss'},{label:'com',value:'com'},{label:'formatting',value:'formatting'},{label:'transactions',value:'transactions'},{label:'eclipse-plugin',value:'eclipse-plugin'},{label:'jar',value:'jar'},{label:'download',value:'download'},{label:'oauth',value:'oauth'},{label:'bluetooth',value:'bluetooth'},{label:'f#',value:'f#'},{label:'amazon-s3',value:'amazon-s3'},{label:'tikz-pgf',value:'tikz-pgf'},{label:'path',value:'path'},{label:'ios6',value:'ios6'},
        {label:'charts',value:'charts'},{label:'solr',value:'solr'},{label:'logic',value:'logic'},{label:'navigation',value:'navigation'},{label:'rspec',value:'rspec'},{label:'header',value:'header'},{label:'functions',value:'functions'},{label:'filter',value:'filter'},{label:'c++11',value:'c++11'},{label:'background',value:'background'},{label:'maven-2',value:'maven-2'},{label:'mac',value:'mac'},{label:'colors',value:'colors'},{label:'smtp',value:'smtp'},{label:'build',value:'build'},{label:'tags',value:'tags'},{label:'microsoft-excel',value:'microsoft-excel'},{label:'msbuild',value:'msbuild'},{label:'tfs',value:'tfs'},{label:'windows-vista',value:'windows-vista'},{label:'open-source',value:'open-source'},{label:'3d',value:'3d'},{label:'virtualbox',value:'virtualbox'},{label:'functional-analysis',value:'functional-analysis'},{label:'module',value:'module'},{label:'compilation',value:'compilation'},{label:'crash',value:'crash'},{label:'automation',value:'automation'},{label:'jboss',value:'jboss'},{label:'documentation',value:'documentation'},{label:'wireless-networking',value:'wireless-networking'},{label:'assembly',value:'assembly'},{label:'ip',value:'ip'},{label:'outlook',value:'outlook'},{label:'usb',value:'usb'},{label:'vpn',value:'vpn'},{label:'windows-server-2008-r2',value:'windows-server-2008-r2'},{label:'hard-drive',value:'hard-drive'},{label:'hadoop',value:'hadoop'},{label:'dependency-injection',value:'dependency-injection'},{label:'2010',value:'2010'},{label:'virtualization',value:'virtualization'},{label:'boot',value:'boot'},{label:'reference-request',value:'reference-request'},{label:'router',value:'router'},{label:'misc',value:'misc'}
    ]
});

function openForm() {
    document.getElementById("myForm").style.display = "block";
}

function closeForm() {
    document.getElementById("myForm").style.display = "none";
}

function set() {
    if(arr.length==0) {
        var t="all";
    }
    else {
        var t="",i=0;
        for(i=0;i<arr.length-1;i++) {
            t+=arr[i];
            t+="_";
        }
        t+=arr[arr.length-1];
    }    
    window.location.href="http://localhost:5000/questions/"+t+"/1";
}
