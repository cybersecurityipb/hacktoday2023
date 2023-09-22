FROM php:7.2-fpm

# Install system dependencies
RUN apt-get update && apt-get install -y \
    git \
    curl \
    libpng-dev \
    libonig-dev \
    libxml2-dev \
    zip \
    unzip

# Clear cache
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Install PHP extensions
RUN docker-php-ext-install pdo_mysql mbstring exif pcntl bcmath gd
RUN curl -sS https://getcomposer.org/installer​ | php -- \
     --install-dir=/usr/local/bin --filename=composer
# Get latest Composer
COPY --from=composer:latest /usr/bin/composer /usr/bin/composer

# Copy Flag
COPY php/flag /flag
COPY php/readflag /readflag
RUN chmod 400 /flag
RUN chmod u+s /readflag

# Copy apps
COPY ../application /var/www/html
RUN chown -R www-data:www-data /var/www/html/storage