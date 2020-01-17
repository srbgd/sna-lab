FROM fluent/fluentd

RUN apk add --no-cache bash make gcc libc-dev ruby-dev \
    && gem install fluent-plugin-mongo \
    && apk del make gcc libc-dev ruby-dev \
    && rm -rf /var/cache/apk/* \
    && rm -rf /tmp/* /var/tmp/* /usr/lib/ruby/gems/*/cache/*.gem
