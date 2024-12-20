FROM ruby:2.7.4

WORKDIR /myapp
COPY . /myapp

# Update RubyGems to ensure compatibility
RUN gem install rubygems-update -v 3.2.33 && update_rubygems

# Install Bundler and Jekyll
RUN gem install bundler -v 2.4.22
RUN gem install jekyll -v 3.9.3
RUN gem install kramdown -v 2.3.1
RUN gem install kramdown-parser-gfm

# Ensure Bundler version matches Gemfile.lock or update it
RUN bundle update --bundler
# Install dependencies from Gemfile
RUN bundle install

EXPOSE 4000

CMD bundle exec jekyll s --host "0.0.0.0" --safe --config _config.yml,_config_local.yml
