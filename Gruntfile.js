module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    
    scsslint: {
      allFiles: [
        'site/themes/ccczh/static/scss/main.scss',
      ]
    },
    sass: {                             
      dist: {                            
        options: {                       
          style: 'expandet' //'expanded' // or compressed
        },
        files: {                         
          'site/themes/ccczh/static/build/css/main.css': 'site/themes/ccczh/static/scss/main.scss'
        }
      }
    },
    csslint: {
      strict: {
        options: {
          import: 2
        },
        src: ['site/themes/ccczh/static/build/css/main.css']
      }
    },

    watch: {

      options: {
        livereload: true,
        spawn: false
      },

      scss: {
        files: 'site/themes/ccczh/static/scss/*.scss',
        tasks: ['scsslint','sass']
      },
    }

  });

  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-scss-lint');
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-csslint');

  grunt.registerTask('default', ['scsslint','sass','csslint']);

};